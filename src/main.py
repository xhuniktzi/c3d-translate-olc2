from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from compiler.statements.define_procedure import DefineProcedure
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """

CREATE PROCEDURE prueba (@valor INT)
AS
BEGIN
	SELECT @valor;
END
    DECLARE @data1 AS INT;
    SET @data1 = 5;

    EXEC prueba ( @valor = @data1);
    SET @data1 = 10;
    EXEC prueba ( @valor = @data1);
    DECLARE @data2 AS INT;
    SET @data2 = 15;
    EXEC prueba ( @valor = @data2);
    """

    old_textoAnalizar: str = """

"""

    textoAnalizar_old: str = """


        """

    lexer.input(textoAnalizar)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    generator: Generator = Generator()
    ast: list[Statement] = parser.parse(textoAnalizar)
    global_env: Environment = Environment()

    for statement in ast:
        # if isinstance(statement, DefineProcedure):
        #     statement.translate_to_c3d(global_env)
        # else:
        statement.translate_to_c3d(global_env)

    print(generator.generate_code())


if __name__ == "__main__":
    main()
