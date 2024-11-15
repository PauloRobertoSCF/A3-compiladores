from parser import parser

# Exemplo de código para testar
data = '''
programa
    inteiro x;
    decimal y;
    x := 10;
    y := x + 3.5;
    if (x > y) escreva y;
    fimprog
'''

# Executa o parser no código de teste
parser.parse(data)
 
