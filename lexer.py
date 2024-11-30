import ply.lex as lex  # Importa a biblioteca PLY (Python Lex-Yacc) para análise léxica

# Lista de tokens para a linguagem fictícia
tokens = [
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',  # Tokens para operações matemáticas
    'ASSIGN', 'LPAREN', 'RPAREN', 'SEMI', 'IF', 'ELSE', 'WHILE', 'FOR',  # Tokens para controle de fluxo e estrutura de programação
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',  # Tokens para operadores relacionais
    'STRING', 'READ', 'WRITE', 'PROGRAM', 'END_PROGRAM'  # Tokens para palavras reservadas
]

# Palavras reservadas // Mapeamento para comandos
reserved = {
    'inteiro': 'INT_TYPE',  # Tipo de dado inteiro
    'decimal': 'FLOAT_TYPE',  # Tipo de dado decimal
    'texto': 'STRING_TYPE',  # Tipo de dado string
    'leia': 'READ',  # Comando de leitura
    'escreva': 'WRITE',  # Comando de escrita
    'programa': 'PROGRAM',  # Início do programa
    'fimprog': 'END_PROGRAM',  # Fim do programa
    'se': 'IF',  # Comando if
    'senão': 'ELSE',  # Comando else
    'enquanto': 'WHILE',  # Comando while
    'para': 'FOR'  # Comando for
}
tokens += list(reserved.values())  # Adiciona as palavras reservadas à lista de tokens

# Definição dos tokens por expressões regulares (regex)
t_PLUS = r'\+' 
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Expressões regulares para capturar identificadores (variáveis) e números
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # Expressão regular para capturar identificadores (variáveis)
    t.type = reserved.get(t.value, 'ID')  # Verifica se o identificador é uma palavra reservada
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'  # Expressão regular para capturar números inteiros e decimais
    t.value = float(t.value) if '.' in t.value else int(t.value)  # Converte o número para float ou int
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'  # Expressão regular para capturar strings (entre aspas duplas)
    return t

# Ignora espaços e tabulações
t_ignore = ' \t'  # Define que espaços e tabulações não geram tokens

# Tratamento de nova linha
def t_newline(t):
    r'\n+'  # Expressão regular para capturar nova linha (quebras de linha)
    t.lexer.lineno += len(t.value)  # A cada nova linha, incrementa o número da linha no lexer

# Erros de caracteres ilegais
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]} na linha {t.lineno}")  # Se o lexer encontrar um caractere ilegal
    t.lexer.skip(1)  # Ignora o caractere inválido e continua a análise

# Constrói o analisador léxico
lexer = lex.lex()  # Cria o analisador léxico a partir das definições acima
