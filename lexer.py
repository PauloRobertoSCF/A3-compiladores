# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'NUMBER', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'SEMI', 'LT', 'GT', 'EQ', 'NE', 'LE', 'GE'
]

# Palavras reservadas
reserved = {
    'inteiro': 'INT_TYPE',
    'decimal': 'FLOAT_TYPE',
    'texto': 'STRING_TYPE',
    'programa': 'PROGRAM',
    'fimprog': 'END_PROGRAM',
    'se': 'IF',
    'senao': 'ELSE',
    'enquanto': 'WHILE',
    'leia': 'READ',
    'escreva': 'WRITE',
}

tokens += list(reserved.values())

# Definição de expressões regulares para os tokens
t_ASSIGN = r':='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NE = r'!='
t_LE = r'<='
t_GE = r'>='

# Token para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra reservada
    return t

# Token para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Função para criar o lexer
def create_lexer():
    return lex.lex()
