import ply.yacc as yacc
from lexer import tokens

# Tabela de símbolos para armazenar variáveis
symbol_table = {}
    'a': 'INT_TYPE',       # a é do tipo inteiro
    'b': 'FLOAT_TYPE',     # b é do tipo decimal (float)
    'nome': 'STRING_TYPE', # nome é do tipo texto (string)
}

# Regras de Produção

def p_program(p):
    '''program : PROGRAM statement_list END_PROGRAM'''
    print("Programa reconhecido.")

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement_decl(p):
    '''statement : INT_TYPE ID SEMI
                 | FLOAT_TYPE ID SEMI
                 | STRING_TYPE ID SEMI'''
    # Adiciona a variável à tabela de símbolos
    symbol_table[p[2]] = p[1]  # Armazena o tipo da variável
    print(f"Declaração de variável: {p[2]} do tipo {p[1]}")

def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMI'''
    # Verifica se a variável foi declarada
    if p[1] not in symbol_table:
        print(f"Erro: A variável {p[1]} não foi declarada.")
        return
    # Verifica o tipo da operação
    var_type = symbol_table[p[1]]
    if isinstance(p[3], float) and var_type == 'INT_TYPE':
        print(f"Erro: Atribuição inválida de número decimal para variável {p[1]} do tipo inteiro.")
        return
    print(f"Atribuição: {p[1]} := {p[3]}")

def p_expression_math(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    # Operação matemática, respeita a precedência
    p[0] = (p[1], p[2], p[3])

def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN statement ELSE statement
                 | IF LPAREN expression RPAREN statement'''
    print("Estrutura de controle if/else reconhecida")

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN statement'''
    print("Estrutura de controle while reconhecida")

def p_statement_for(p):
    '''statement : FOR LPAREN statement SEMI expression SEMI statement RPAREN statement'''
    print("Estrutura de controle for reconhecida")

def p_statement_read(p):
    '''statement : READ ID SEMI'''
    print(f"Ler valor para {p[2]}")

def p_statement_write(p):
    '''statement : WRITE expression SEMI'''
    print(f"Imprimir: {p[2]}")

def p_error(p):
    if p:
        print(f"Erro de sintaxe no token {p.type}, linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Construção do parser
parser = yacc.yacc()

# Função para analisar um programa
def analyze_program(program_code):
    lexer.input(program_code)
    parser.parse(program_code)
# Lexer e Parser implementados anteriormente

# Função de análise do programa
def analyze_program(program_code):
    lexer.input(program_code)
    parser.parse(program_code)

# Função para gerar o código Python a partir da tabela de símbolos
def generate_python_code():
    python_code = ""
    for var, var_type in symbol_table.items():
        if var_type == 'INT_TYPE':
            python_code += f"{var} = 0  # Inteiro\n"
        elif var_type == 'FLOAT_TYPE':
            python_code += f"{var} = 0.0  # Decimal\n"
        elif var_type == 'STRING_TYPE':
            python_code += f"{var} = ''  # String\n"
    
    # Adicionar operações matemáticas simples e expressões
    python_code += "x = a + b * c\n"  # Exemplo de operação matemática

     # Adicionar um exemplo de estrutura de repetição "while"
    python_code += "\n# Estrutura de repetição (while)\n"
    python_code += "while a < 10:\n"
    python_code += "    a += 1\n"
    
    # Adicionar um exemplo de estrutura de repetição "for"
    python_code += "\n# Estrutura de repetição (for)\n"
    python_code += "for i in range(5):\n"
    python_code += "    print(i)\n"
    
    # Exemplo de uma estrutura de controle
    python_code += "if a > b:\n"
    python_code += "    print('Maior')\n"
    python_code += "else:\n"
    python_code += "    print('Menor')\n"
    
    return python_code

# Programa fictício para análise
program_code = '''
programa
    inteiro a;
    decimal b;
    texto c;
    a := 10;
    b := 5.5;
    escreva(a + b);
    se a > b então
        escreva('Maior');
    senão
        escreva('Menor');
    fimprog
'''

# Analisando o programa e gerando código Python
analyze_program(program_code)
generated_code = generate_python_code()

# Exibindo o código Python gerado
print("Código gerado em Python:")
print(generated_code)


