from astcode import ProgramNode, DeclarationNode, AssignmentNode, WriteNode, ReadNode, IfNode, WhileNode, BinaryOpNode, VariableNode, ComparisonNode, ForNode

class PythonCodeGenerator:
    def __init__(self):
        self.code = []
        self.declarations = []  

    def generate(self, node):
        if isinstance(node, ProgramNode):
            for statement in node.statements:
                self.generate(statement)
            self.code = self.declarations + self.code
        elif isinstance(node, DeclarationNode):
            if node.var_type == "inteiro":
                self.declarations.append(f"int {node.var_name}")
            elif node.var_type == "decimal":
                self.declarations.append(f"float {node.var_name}")
            elif node.var_type == "texto":
                self.declarations.append(f"string {node.var_name}")
        elif isinstance(node, AssignmentNode):
            self.code.append(f"{node.var_name} = {self.generate_expression(node.expression)}")
        elif isinstance(node, WriteNode):
            if isinstance(node.expression, list):
                raise TypeError("Erro: 'WriteNode.expression' deveria ser um único valor, não uma lista.")
            self.code.append(f"print({self.generate_expression(node.expression)})")
        elif isinstance(node, ReadNode):
            self.code.append(f"{node.var_name} = input()")
        elif isinstance(node, IfNode):
            cond = self.generate_expression(node.condition)
            self.code.append(f"if {cond}:")
            self.code.append("    " + "\n    ".join(self.generate_block(node.then_branch)))
            if node.else_branch:
                self.code.append("else:")
                self.code.append("    " + "\n    ".join(self.generate_block(node.else_branch)))
        elif isinstance(node, WhileNode):
            cond = self.generate_expression(node.condition)
            self.code.append(f"while {cond}:")
            self.code.append("    " + "\n    ".join(self.generate_block(node.body)))
        elif isinstance(node, ForNode):
            start = self.generate_expression(node.start)
            end = self.generate_expression(node.end)
            step = self.generate_expression(node.step) if node.step else "1"
            self.code.append(f"for {node.variable.var_name} in range({start}, {end}, {step}):")
            self.code.append(" " + "\n ".join(self.generate_block(node.body)))

    def generate_expression(self, expression):
        if isinstance(expression, BinaryOpNode):
            left = self.generate_expression(expression.left)
            right = self.generate_expression(expression.right)
            return f"({left} {expression.operator} {right})"
        elif isinstance(expression, VariableNode):
            return expression.var_name
        elif isinstance(expression, ComparisonNode):
            left = self.generate_expression(expression.left)
            right = self.generate_expression(expression.right)
            return f"({left} {expression.operator} {right})"
        elif isinstance(expression, (int, float, str)):
            return repr(expression)

    def generate_block(self, statements):
        gen = PythonCodeGenerator()
        if isinstance(statements, list):
         for statement in statements:
            gen.generate(statement)

        else: gen.generate(statements)
        return gen.code

    def get_code(self):
        return "\n".join(self.code)
    
    def visit_declaration(self, node):
        default_values = {
            "inteiro": "0",
            "decimal": "0.0",
            "texto": "''",
    }
        default_value = default_values.get(node.var_type, "None")
        self.code.append(f"{node.var_name} = {default_value}")
