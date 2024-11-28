import ply.yacc as yacc
from lexer import tokens  # Importa os tokens definidos no lexer.py
from ast import BinaryOpNode, ASTNode  # Importe o BinaryOpNode e outros nós necessários
# Regras de produção

# Regra inicial (para começar a análise a partir do programa completo)
def p_program(p):
    '''program : PROGRAM statement_list END_PROGRAM'''
    print("Programa reconhecido")

# Lista de declarações ou expressões
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# Declaração de variáveis (tipo seguido de identificador)
def p_statement_decl(p):
    '''statement : INT_TYPE ID SEMI
                 | FLOAT_TYPE ID SEMI
                 | STRING_TYPE ID SEMI'''
    print(f"Declaração de variável: {p[2]}")

# Atribuição de variáveis (ID := expressão)
def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMI'''
    print(f"Atribuição: {p[1]} := {p[3]}")

# Expressões matemáticas (números e operações)
def p_expression_math(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = BinaryOpNode(p[1], p[2], p[3])  # Cria um nó de operação binária
    pass

# Expressão com parênteses (para prioridade)
def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

# Expressão de número ou variável
def p_expression_number(p):
    '''expression : NUMBER
                  | ID'''
    p[0] = p[1]

# Estrutura de controle if-else
def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN statement ELSE statement
                 | IF LPAREN expression RPAREN statement'''
    print("Estrutura de controle if/else reconhecida")

# Estrutura de controle while
def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN statement'''
    print("Estrutura de controle while reconhecida")

# Regra para erros de sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe no token {p.type}, linha {p.lineno}")
        parser.errok()
    else:
        print("Erro de sintaxe no final do arquivo")

# Construção do parser
parser = yacc.yacc()
