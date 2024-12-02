import ply.yacc as yacc
from lexer import tokens
from astcode import ProgramNode, VariableNode, DeclarationNode, AssignmentNode, BinaryOpNode, IfNode, WhileNode, ForNode, WriteNode, ReadNode, ComparisonNode


def p_program(p):
    '''program : PROGRAM statement_list END_PROGRAM'''
    p[0] = ProgramNode(p[2])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | write
                 | read
                 | if_statement
                 | while_statement
                 | for_statement'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : INT_TYPE ID SEMI
                   | FLOAT_TYPE ID SEMI
                   | STRING_TYPE ID SEMI'''
    p[0] = DeclarationNode(p[1].lower(), p[2])

def p_expression_math(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = BinaryOpNode(p[1], p[2], p[3])

def p_expression_id(p):
    """
    expression : ID
    """
    p[0] = VariableNode(p[1])

def p_expression_comparison(p):
    """
    expression : expression LT expression
               | expression GT expression
               | expression LE expression
               | expression GE expression
               | expression EQ expression
               | expression NE expression
    """
    p[0] = ComparisonNode(p[2], p[1], p[3])  

def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMI'''
    p[0] = AssignmentNode(p[1], p[3])

def p_write(p):
    '''write : WRITE expression SEMI'''
    if isinstance(p[2], list):
        raise TypeError("Erro no parser: 'WRITE' recebeu múltiplas expressões.")
    p[0] = WriteNode(p[2])

def p_read(p):
    '''read : READ ID SEMI'''
    p[0] = ReadNode(p[2])

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement ELSE statement
                    | IF LPAREN expression RPAREN statement'''
    if len(p) == 8:
        p[0] = IfNode(p[3], [p[5]], [p[7]])
    else:
        p[0] = IfNode(p[3], [p[5]])

def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN statement'''
    p[0] = WhileNode(p[3], p[5])

def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment SEMI expression SEMI assignment RPAREN statement'''
    p[0] = ForNode(p[3], p[5], p[7], p[9])

def p_expression(p):
    '''expression : term expression_prime'''
    if len(p) == 3 and p[2] is not None:
        p[0] = BinaryOpNode(p[1], p[2][0], p[2][1])
    else:
        p[0] = p[1]

def p_expression_prime(p):
    '''expression_prime : PLUS term
                        | MINUS term
                        | empty'''
    if len(p) == 4:
        p[0] = (p[1], p[2])
    else:
        p[0] = None

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = p[1]  

def p_term(p):
    '''term : factor term_prime'''
    if len(p) == 3 and p[2] is not None:
        p[0] = BinaryOpNode(p[1], p[2][0], p[2][1])
    else:
        p[0] = p[1]

def p_term_prime(p):
    '''term_prime : TIMES factor
                  | DIVIDE factor
                  | empty'''
    if len(p) == 4:
        p[0] = (p[1], p[2])
    else:
        p[0] = None

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print(f"Erro de sintaxe no token {p.type}" if p else "Erro de sintaxe no final do arquivo")


parser = yacc.yacc(debug=True)
