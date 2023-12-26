from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    _textoAnalizar: str = """
    CREATE FUNCTION SUM(@A INT, @B INT)
    RETURN INT
    AS
    BEGIN
        RETURN @A + @B;
    END

    SELECT SUM(@A = 1, @B = 2);

    """

    textoAnalizar: str = """
	CREATE FUNCTION ackermann (@M INT, @N INT)
    RETURN INT
    AS
	BEGIN
		IF (@M == 0)
		BEGIN
			RETURN @N + 1;
		END

        IF (@M > 0 && @N == 0)
        BEGIN
            RETURN ackermann(@M = @M - 1, @N = 1);
        END

        IF (@M > 0 && @N > 0)
        BEGIN
            RETURN ackermann(@M = @M - 1, @N =  ackermann(@M = @M, @N = @N - 1));
        END
    END
    
    SELECT ackermann(@M = 0,@N = 0);
    SELECT ackermann(@M = 1,@N = 1);
    SELECT ackermann(@M = 2,@N = 2);
    SELECT ackermann(@M = 3,@N = 3);
    SELECT ackermann(@M = 4,@N = 0);
    SELECT ackermann(@M = 4,@N = 1);
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
        statement.translate_to_c3d(global_env)

    with open("src/main.c", "w") as file:
        file.write(generator.generate_code())


if __name__ == "__main__":
    main()
