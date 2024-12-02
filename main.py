from parsercode import parser
import ply.yacc as yacc
from lexer import create_lexer
from semantic import SemanticAnalyzer
from code_generator import PythonCodeGenerator
from astcode import ProgramNode


if __name__ == "__main__":
    # Código fictício de entrada
    program_code = """
programa
    inteiro a;
    decimal b;
    texto c;

    a := 10;
    b := 3.14;
    c := "oi";

    escreva a;
    escreva b;
    escreva c;

    se (a < 9)
        escreva "a < 9";
    senao
        escreva "a >= 9";

    enquanto (a > 0)
        escreva a;
        a := a - 1;

    para (a := 0; a < 5; a := a + 1)
        escreva a;
fimprog
    """

    # Lexer e Parser
    lexer = create_lexer()
    parser = yacc.yacc(debug=True)
    astcode = parser.parse(program_code, lexer=lexer)

    # Análise Semântica
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze_program(ProgramNode)

    # Geração de Código Python
    code_generator = PythonCodeGenerator()
    code_generator.generate(ProgramNode) 
    code = code_generator.get_code()

    # Exibir código gerado
    print("Código Python Gerado:")
    print(code)
