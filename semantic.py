class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = [{}]  # Pilha de escopos (cada escopo é um dicionário)

    def enter_scope(self):
        """Entra em um novo escopo (como dentro de um 'if' ou 'while')."""
        self.symbol_table.append({})

    def exit_scope(self):
        """Sai do escopo atual."""
        if len(self.symbol_table) > 1:
            self.symbol_table.pop()
        else:
            raise SemanticError("Erro: Tentativa de sair do escopo global.")

    def declare_variable(self, var_name, var_type):
        """Declara uma variável no escopo atual."""
        current_scope = self.symbol_table[-1]
        if var_name in current_scope:
            raise SemanticError(f"Erro: Variável '{var_name}' já declarada neste escopo.")
        current_scope[var_name] = var_type

    def check_variable(self, var_name):
        """Verifica se a variável foi declarada em qualquer escopo visível."""
        for scope in reversed(self.symbol_table):
            if var_name in scope:
                return scope[var_name]
        raise SemanticError(f"Erro: Variável '{var_name}' não declarada.")

    def check_assignment(self, var_name, value_type):
        """Valida a atribuição de tipo."""
        var_type = self.check_variable(var_name)
        if var_type != value_type:
            if var_type == "inteiro" and value_type == "decimal":
                # Permitir conversão implícita
                return
            raise SemanticError(f"Erro: Atribuição incompatível. Esperado '{var_type}', recebido '{value_type}'.")

    def check_operation(self, left_type, right_type, operator):
    """Valida operações entre tipos."""
    if left_type == right_type == "inteiro":
        return "inteiro"  # Retorna tipo inteiro se ambos os operandos forem inteiros
    elif (left_type, right_type) in [("inteiro", "decimal"), ("decimal", "inteiro"), ("decimal", "decimal")]:
        return "decimal"  # Operações com decimais resultam em decimal
    else:
        raise SemanticError(f"Operação '{operator}' inválida entre '{left_type}' e '{right_type}'.")


class SemanticError(Exception):
    """Classe para representar erros semânticos."""
    pass
 
 if __name__ == "__main__":
    analyzer = SemanticAnalyzer()
    try:
        analyzer.analyze_program(program_ast)
        print("Análise semântica concluída com sucesso.")
    except SemanticError as e:
        print(f"Erro semântico: {e}")


 
