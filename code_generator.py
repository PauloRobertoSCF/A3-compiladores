import astcode

class CodeGenerator:
    def __init__(self):
        self.code = []

    def visit_program(self, node):
        for stmt in node.statements:
            stmt.accept(self)
        return "\n".join(self.code)

    def visit_declaration(self, node):
        self.code.append(f"{node.var_type} {node.var_name};")

    def visit_assignment(self, node):
        expr = node.expression.accept(self)
        self.code.append(f"{node.var_name} = {expr};")

   def visit_binary_op(self, node):
    left_code = node.left.accept(self)
    right_code = node.right.accept(self)
    return f"({left_code} {node.operator} {right_code})"

    def visit_if(self, node):
        condition = node.condition.accept(self)
        self.code.append(f"if ({condition}) {{")
        for stmt in node.then_branch:
            stmt.accept(self)
        self.code.append("}")
        if node.else_branch:
            self.code.append("else {")
            for stmt in node.else_branch:
                stmt.accept(self)
            self.code.append("}")

    def visit_while(self, node):
        condition = node.condition.accept(self)
        self.code.append(f"while ({condition}) {{")
        for stmt in node.body:
            stmt.accept(self)
        self.code.append("}")

    def visit_write(self, node):
        expr = node.expression.accept(self)
        self.code.append(f"print({expr});")

    def visit_read(self, node):
        self.code.append(f"input({node.var_name});")

# Código auxiliar para expressões simples
    def visit(self, node):
        return node.accept(self)

