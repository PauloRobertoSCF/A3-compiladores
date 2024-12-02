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

class StatementNode(ASTNode):
    def init(self, statement):
        super().init()
        self.statement = statement  

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
    """Nó para operações binárias (e.g., soma, subtração, multiplicação)."""
    def __init__(self, left, operator, right):
        self.left = left       
        self.operator = operator  
        self.right = right     

    def accept(self, visitor):
        return visitor.visit_binary_op(self)


class VariableNode(ASTNode):
    """Nó para variáveis (usado em expressões ou atribuições)."""
    def __init__(self, var_name):
        self.var_name = var_name  

    def accept(self, visitor):
        """Permite que o visitante (visitor) passe por este nó."""
        return visitor.visit_variable(self)


class IfNode(ASTNode):
    """Nó para estruturas condicionais."""
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = [then_branch] if not isinstance(then_branch, list) else then_branch
        self.else_branch = [else_branch] if else_branch and not isinstance(else_branch, list) else else_branch

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
    
class ForNode(ASTNode):
    def __init__(self, variable, start, end, step, body):
        """
        Representa um nó de laço 'for' na AST.

        :param variable: A variável de controle do laço (ex.: 'i').
        :param start: O valor inicial do laço.
        :param end: A condição de parada ou valor final do laço.
        :param step: O incremento ou passo do laço (pode ser None).
        :param body: O corpo do laço (uma lista de nós de instruções).
        """
        self.variable = variable  
        self.start = start        
        self.end = end            
        self.step = step          
        self.body = body         
    def accept(self, visitor): 
        return visitor.visit_for(self)

    def repr(self):
        """Representação legível para depuração."""
        return (f"ForNode(variable={self.variable}, start={self.start}, "
                f"end={self.end}, step={self.step}, body={self.body})")
    def accept(self, visitor):
        return visitor.visit_for(self)

class ComparisonNode:
    def __init__(self, operator, left, right):
        """
        Inicializa o nó de comparação.

        :param operator: Operador da comparação (e.g., '<', '>', '==')
        :param left: Expressão à esquerda do operador
        :param right: Expressão à direita do operador
        """
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Representação do nó para depuração.
        """
        return f"ComparisonNode(operator='{self.operator}', left={self.left}, right={self.right})"

    def evaluate(self, context):
        """
        Avalia o nó de comparação no contexto atual (opcional).

        :param context: Um dicionário ou objeto que mapeia variáveis para valores.
        :return: O resultado booleano da comparação.
        """
        left_value = self.left.evaluate(context) if isinstance(self.left, ASTNode) else self.left
        right_value = self.right.evaluate(context) if isinstance(self.right, ASTNode) else self.right

        if self.operator == '<':
            return left_value < right_value
        elif self.operator == '>':
            return left_value > right_value
        elif self.operator == '<=':
            return left_value <= right_value
        elif self.operator == '>=':
            return left_value >= right_value
        elif self.operator == '==':
            return left_value == right_value
        elif self.operator == '!=':
            return left_value != right_value
        else:
            raise ValueError(f"Operador desconhecido: {self.operator}")

