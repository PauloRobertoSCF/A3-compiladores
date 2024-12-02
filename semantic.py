from astcode import ProgramNode, DeclarationNode, AssignmentNode, BinaryOpNode, IfNode, WhileNode, ForNode, WriteNode, ReadNode, VariableNode, ComparisonNode


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = [{}]
        self.symbol_table[-1]['a'] = 'inteiro'  # Declarando 'a' como inteiro
        self.symbol_table[-1]['b'] = 'decimal'  # Declarando 'b' como decimal
        self.symbol_table[-1]['c'] = 'texto'

    def enter_scope(self):
        """Entra em um novo escopo."""
        self.symbol_table.append({})

    def exit_scope(self):
        """Sai do escopo atual."""
        if len(self.symbol_table) > 1:
            self.symbol_table.pop()
        else:
            raise Exception("Erro: Tentativa de sair do escopo global.")
        
    def declare_variable(self, var_name, var_type):
        """Declara ou redefine uma variável no escopo atual."""
        current_scope = self.symbol_table[-1]
        current_scope[var_name] = var_type

    def analyze_program(self, node):
        """Inicia a análise semântica do programa."""
        if isinstance(node, ProgramNode):
            for statement in node.statements:
                self.analyze_program(statement)
        elif isinstance(node, DeclarationNode):
            self.declare_variable(node.var_name, node.var_type)
        elif isinstance(node, AssignmentNode):
            var_type = self.check_variable(node.var_name)
            expr_type = self.analyze_expression(node.expression)
            if var_type == expr_type or (var_type == "decimal" and expr_type == "inteiro"):
                    # Permitir conversão implícita de decimal para inteiro
                return
            raise Exception(f"Erro: Atribuição incompatível. '{node.var_name}' é do tipo '{var_type}', mas recebeu '{expr_type}'.")
        elif isinstance(node, BinaryOpNode):
            left_type = self.analyze_expression(node.left)
            right_type = self.analyze_expression(node.right)
            if left_type != right_type:
                raise Exception(f"Erro: Operação inválida entre '{left_type}' e '{right_type}'.")
        elif isinstance(node, IfNode):
            cond_type = self.analyze_expression(node.condition)
            if cond_type not in ["inteiro", "decimal"]:
                raise Exception("Erro: Condição de 'if' deve ser do tipo 'inteiro' ou 'decimal'.")
            self.enter_scope()
            self.analyze_program(node.then_branch)
            if node.else_branch:
                self.analyze_program(node.else_branch)
            self.exit_scope()
        elif isinstance(node, ForNode): # Certificar que as variáveis estão corretamente declaradas e analisadas
            self.analyze_program(node.start)
            cond_type = self.analyze_expression(node.end)
            if cond_type not in ["inteiro", "decimal"]:
                raise Exception("Erro: Condição de 'for' deve ser do tipo 'inteiro' ou 'decimal'.")
            self.enter_scope()
            self.analyze_program(node.body)
            self.exit_scope()
        elif isinstance(node, WhileNode):
            cond_type = self.analyze_expression(node.condition)
            if cond_type != "inteiro":
                raise Exception("Erro: Condição de 'while' deve ser do tipo 'inteiro'.")
            self.enter_scope()
            self.analyze_program(node.body)
            self.exit_scope()
        elif isinstance(node, WriteNode):
            expr_type = self.analyze_expression(node.expression)
            if expr_type not in ["inteiro", "decimal", "texto"]:
                raise Exception(f"Erro: Tipo '{expr_type}' inválido para 'escreva'.")
        elif isinstance(node, ReadNode):
            self.check_variable(node.var_name)

    def check_variable(self, var_name):
        """Verifica se a variável foi declarada em algum escopo visível."""
        for scope in reversed(self.symbol_table):
            if var_name in scope:
                return scope[var_name]
        raise Exception(f"Erro: Variável '{var_name}' não declarada.")

    def analyze_expression(self, expression):
        if isinstance(expression, BinaryOpNode):
            left_type = self.analyze_expression(expression.left)
            right_type = self.analyze_expression(expression.right)
            # Permitir concatenação de texto
            if left_type == "texto" and right_type == "texto" and expression.operator == "+":
                return "texto"
            # Promoção entre decimal e inteiro
            if left_type == right_type:
                return left_type
            if left_type == "inteiro" and right_type == "decimal":
                return "decimal"
            if left_type == "decimal" and right_type == "inteiro":
                return "decimal"
            raise Exception(f"Erro: Operação inválida entre '{left_type}' e '{right_type}'.")
        elif isinstance(expression, VariableNode):
            return self.check_variable(expression.var_name)
        elif isinstance(expression, ComparisonNode):
            left_type = self.analyze_expression(expression.left)
            right_type = self.analyze_expression(expression.right)
            if left_type == right_type:
                return "inteiro"  # Comparações resultam em 'inteiro' para compatibilidade
            raise Exception(f"Erro: Comparação entre tipos incompatíveis: '{left_type}' e '{right_type}'.")
        elif isinstance(expression, int):
            return "inteiro"
        elif isinstance(expression, float):
            return "decimal"
        elif isinstance(expression, str):
            return "texto"

 
