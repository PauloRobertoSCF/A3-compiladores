# parser.py
import ply.yacc as yacc
from lexer import tokens
from astcode import ProgramNode, DeclarationNode, AssignmentNode, BinaryOpNode, IfNode, WhileNode, WriteNode, ReadNode

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

def p_statement_decl(p):
    '''statement : INT_TYPE ID SEMI
                 | FLOAT_TYPE ID SEMI
                 | STRING_TYPE ID SEMI'''
    p[0] = DeclarationNode(p[2], p[1].lower())

def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMI'''
    p[0] = AssignmentNode(p[1], p[3])

def p_statement_write(p):
    '''statement : WRITE expression SEMI'''
    p[0] = WriteNode(p[2])

def p_expression_math(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = BinaryOpNode(p[1], p[2], p[3])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Erro de sintaxe no token {p.type}, linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Criar o parser
parser = yacc.yacc()


