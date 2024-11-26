import sys
from lexer import lexer
from parser import parser
from semantic import SemanticAnalyzer, SemanticError
from code_generator import CodeGenerator
from ast import

def main():
    # Solicita ao usuário um arquivo de entrada
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo>")
        return

    input_file = sys.argv[1]
    
    try:
        # Lê o código fonte do arquivo
        with open(input_file, 'r') as f:
            source_code = f.read()

        print("\n=== CÓDIGO FONTE ===")
        print(source_code)

        # === Etapa 1: Análise Léxica ===
        print("\n=== ANÁLISE LÉXICA ===")
        lexer.input(source_code)
        while True:
            token = lexer.token()
            if not token:
                break
            print(token)

        # === Etapa 2: Análise Sintática ===
        print("\n=== ANÁLISE SINTÁTICA ===")
        ast = parser.parse(source_code, lexer=lexer)
        if ast is None:
            print("Erro na análise sintática.")
            return

        print("AST gerada com sucesso.")

        # === Etapa 3: Análise Semântica ===
        print("\n=== ANÁLISE SEMÂNTICA ===")
        analyzer = SemanticAnalyzer()
        try:
            analyzer.analyze_program(ast)  # O método `analyze_program` percorre a AST para validações semânticas
            print("Análise semântica concluída com sucesso.")
        except SemanticError as e:
            print(f"Erro semântico: {e}")
            return

        # === Etapa 4: Geração de Código ===
        print("\n=== GERAÇÃO DE CÓDIGO ===")
        generator = CodeGenerator()
        target_code = generator.generate_code(ast)

        print("\n=== CÓDIGO GERADO ===")
        print(target_code)

        # Opcional: Escrever o código gerado em um arquivo de saída
        output_file = input_file.replace('.txt', '_output.txt')
        with open(output_file, 'w') as f:
            f.write(target_code)

        print(f"\nCódigo gerado salvo em: {output_file}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
