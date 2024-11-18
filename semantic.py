 class SemanticAnalyzer:
    def __init__(self):
        # Tabela de símbolos para rastrear variáveis e seus tipos
        self.symbol_table = {}

    def declare_variable(self, var_name, var_type):
        """
        Declara uma variável e verifica se ela já foi declarada.
        """
        if var_name in self.symbol_table:
            raise SemanticError(f"Erro: Variável '{var_name}' já foi declarada.")
        self.symbol_table[var_name] = var_type

    def check_variable(self, var_name):
        """
        Verifica se uma variável foi declarada antes do uso.
        """
        if var_name not in self.symbol_table:
            raise SemanticError(f"Erro: Variável '{var_name}' não foi declarada.")

    def check_assignment(self, var_name, value_type):
        """
        Verifica se a atribuição é válida em relação ao tipo da variável.
        """
        self.check_variable(var_name)
        var_type = self.symbol_table[var_name]
        if var_type == "inteiro" and value_type == "decimal":
            raise SemanticError(
                f"Erro: Não é possível atribuir um valor do tipo 'decimal' a uma variável do tipo 'inteiro'."
            )

    def check_operation(self, left_type, right_type):
        """
        Verifica se uma operação é válida entre dois tipos.
        """
        if left_type == "inteiro" and right_type == "decimal":
            return "decimal"
        if left_type == "decimal" and right_type == "inteiro":
            return "decimal"
        if left_type == right_type:
            return left_type
        raise SemanticError(f"Erro: Operação inválida entre '{left_type}' e '{right_type}'.")

    def check_condition(self, var_name):
        """
        Verifica se a variável em uma condição é válida.
        """
        self.check_variable(var_name)


class SemanticError(Exception):
    """
    Classe de exceção para erros semânticos.
    """
    pass


# Exemplo de uso do analisador semântico
if __name__ == "__main__":
    analyzer = SemanticAnalyzer()

    # Exemplo de programa analisado semanticamente
    try:
        # Declarações
        analyzer.declare_variable("x", "inteiro")
        analyzer.declare_variable("y", "decimal")

        # Atribuições
        analyzer.check_assignment("x", "inteiro")  # x := 10;
        analyzer.check_assignment("y", "decimal")  # y := x + 3.5;

        # Operações
        result_type = analyzer.check_operation("inteiro", "decimal")

        # Condições
        analyzer.check_condition("x")
        analyzer.check_condition("y")

        print("Análise semântica concluída sem erros.")
    except SemanticError as e:
        print(e)
