class ASTNode:
    """Classe base para todos os nós da AST."""
    def accept(self, visitor):
        """Método para aceitar visitantes (padrão Visitor)."""
        raise NotImplementedError("Este método deve ser implementado nas subclasses")


class ProgramNode(ASTNode):
    """Nó principal que representa o programa."""
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        return visitor.visit_program(self)


class DeclarationNode(ASTNode):
    """Nó para declarações de variáveis."""
    def __init__(self, var_type, var_name):
        self.var_type = var_type
        self.var_name = var_name

    def accept(self, visitor):
        return visitor.visit_declaration(self)


class AssignmentNode(ASTNode):
    """Nó para atribuições."""
    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_assignment(self)


class BinaryOpNode(ASTNode):
    """Nó para operações binárias (e.g., soma, subtração)."""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_binary_op(self)


class IfNode(ASTNode):
    """Nó para estruturas condicionais."""
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def accept(self, visitor):
        return visitor.visit_if(self)


class WhileNode(ASTNode):
    """Nó para laços 'while'."""
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def accept(self, visitor):
        return visitor.visit_while(self)


class WriteNode(ASTNode):
    """Nó para instruções 'escreva'."""
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_write(self)


class ReadNode(ASTNode):
    """Nó para instruções 'leia'."""
    def __init__(self, var_name):
        self.var_name = var_name

    def accept(self, visitor):
        return visitor.visit_read(self)

