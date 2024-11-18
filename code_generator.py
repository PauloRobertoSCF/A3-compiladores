class CodeGenerator:
    def __init__(self):
        self.output = []  # Lista para armazenar as linhas de código gerado
        self.indent_level = 0  # Controle de indentação

    def emit(self, line):
        """
        Adiciona uma linha ao código gerado, respeitando o nível de indentação.
        """
        indentation = "    " * self.indent_level
        self.output.append(f"{indentation}{line}")

    def declare_variable(self, var_name, var_type):
        """
        Gera código para declarar uma variável com inicialização padrão.
        """
        default_value = "0" if var_type == "inteiro" else "0.0"
        self.emit(f"{var_name} = {default_value}")

    def assign_value(self, var_name, expression):
        """
        Gera código para uma atribuição.
        """
        self.emit(f"{var_name} = {expression}")

    def generate_condition(self, condition):
        """
        Gera código para uma estrutura condicional.
        """
        self.emit(f"if {condition}:")

    def write_statement(self, expression):
        """
        Gera código para um comando de saída (print).
        """
        self.emit(f"print({expression})")

    def increase_indent(self):
        """
        Aumenta o nível de indentação.
        """
        self.indent_level += 1

    def decrease_indent(self):
        """
        Diminui o nível de indentação.
        """
        if self.indent_level > 0:
            self.indent_level -= 1

    def generate(self):
        """
        Retorna o código gerado como uma única string.
        """
        return "\n".join(self.output)


# Exemplo de uso do gerador de código
if __name__ == "__main__":
    generator = CodeGenerator()

    # Simulação do processo de geração de código
    generator.declare_variable("x", "inteiro")
    generator.declare_variable("y", "decimal")
    generator.assign_value("x", "10")
    generator.assign_value("y", "x + 3.5")
    generator.generate_condition("x > y")
    generator.increase_indent()
    generator.write_statement("y")
    generator.decrease_indent()

    # Gerar e exibir o código Python
    generated_code = generator.generate()
    print("Código Gerado:")
    print(generated_code)
 
