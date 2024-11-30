import ply.yacc as yacc
from lexer import tokens
from ast import BinaryOpNode, UnaryOpNode, AssignNode, WriteNode, ReadNode, VarDeclNode, IfNode, WhileNode, ProgramNode

# Programa completo
def p_program(p):
    '''program : PROGRAM statement_list END_PROGRAM'''
    # Cria o nó principal do programa
    p[0] = ProgramNode(p[2])
    print("Programa reconhecido")

# Lista de declarações ou comandos
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 2:  # Apenas um statement
        p[0] = [p[1]]
    else:  # Combina vários statements em uma lista
        p[0] = p[1] + [p[2]]

# Declaração de variáveis
def p_statement_decl(p):
    '''statement : INT_TYPE ID_LIST SEMI
                 | FLOAT_TYPE ID_LIST SEMI
                 | STRING_TYPE ID_LIST SEMI'''
    # Cria nós de declaração de variável para cada ID
    p[0] = [VarDeclNode(p[1], var) for var in p[2]]
    print(f"Declaração de variáveis: {p[2]} do tipo {p[1]}")

def p_id_list(p):
    '''ID_LIST : ID
               | ID COMMA ID_LIST'''
    if len(p) == 2:  # Apenas um identificador
        p[0] = [p[1]]
    else:  # Lista de identificadores separados por vírgula
        p[0] = [p[1]] + p[3]

# Atribuição de valores a variáveis
def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMI'''
    # Cria um nó de atribuição
    p[0] = AssignNode(p[1], p[3])
    print(f"Atribuição: {p[1]} := {p[3]}")

# Comandos leia e escreva
def p_statement_read(p):
    '''statement : READ LPAREN ID RPAREN SEMI'''
    # Cria um nó para o comando leia
    p[0] = ReadNode(p[3])
    print(f"Comando leia: {p[3]}")

def p_statement_write(p):
    '''statement : WRITE LPAREN expression RPAREN SEMI'''
    # Cria um nó para o comando escreva
    p[0] = WriteNode(p[3])
    print(f"Comando escreva: {p[3]}")

# Estruturas de controle if e if-else
def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN statement ELSE statement
                 | IF LPAREN expression RPAREN statement'''
    if len(p) == 6:  # if sem else
        p[0] = IfNode(p[3], p[5], None)
        print("Estrutura if reconhecida (sem else)")
    else:  # if com else
        p[0] = IfNode(p[3], p[5], p[7])
        print("Estrutura if/else reconhecida")

# Estrutura de controle while
def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN statement'''
    # Cria um nó para a estrutura while
    p[0] = WhileNode(p[3], p[5])
    print("Estrutura while reconhecida")

# Expressões matemáticas
def p_expression_math(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    # Cria um nó binário para operações matemáticas
    p[0] = BinaryOpNode(p[2], p[1], p[3])
    print(f"Operação matemática: {p[1]} {p[2]} {p[3]}")

# Expressões com parênteses
def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]
    print(f"Expressão com parênteses: ({p[2]})")

# Expressão de número ou variável
def p_expression_term(p):
    '''expression : NUMBER
                  | ID'''
    p[0] = p[1]
    print(f"Expressão: {p[1]}")

# Erro na análise sintática
def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}' (tipo {p.type}), linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Construção do parser
parser = yacc.yacc()

