from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar = """
    DECLARE @numero AS INT;
    SET @numero = 10;


        """

    otrotext: str = """

        SELECT @numero;
    IF (@a > @b) BEGIN
        SET @resultado = @a;
    END

    IF (@x == @y) BEGIN
        SET @mensaje = "Iguales";
    END ELSE BEGIN
        SET @mensaje = "Diferentes";
    END

    WHILE (@contador < 10) BEGIN
        SET @contador = @contador + 1;
    END

    EXEC ProcedimientoSumar(@param1 = 5, @param2 = 10);

    CREATE PROCEDURE CalcularMaximo (@a INT, @b INT) BEGIN
        IF (@a > @b) BEGIN
            SELECT @a;
        END ELSE BEGIN
            SELECT @b;
        END
    END

        IF (((@a + @b) / 2 > 10 && @c != NULL) || @d == 0) BEGIN
        SET @resultado = "Complejo";
    END

      CREATE PROCEDURE test (@a INT, @b INT, @c INT) BEGIN
        DECLARE @d AS INT;
        SET @d = 1;
        
        IF (@a > @b) BEGIN 
            SET @c = @a;
            END
        ELSE BEGIN
            SET @c = @b;
        END
        WHILE (@d < 10) BEGIN
            SET @d = @d + 1;
        END
        SELECT @c;
        END

    
    DECLARE @i AS INT;
    SET @i = 0;
    WHILE (@i < 5) BEGIN
        IF (@i == 3) BEGIN
            SET @mensaje = "Tres";
        END ELSE BEGIN
            SET @mensaje = "Otro número";
        END
        SET @i = @i + 1;
    END
    """

    lexer.input(textoAnalizar)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    generator: Generator = Generator()
    ast: list[Statement] = parser.parse(textoAnalizar)
    global_env: Environment = Environment(None)
    for statement in ast:
        statement.translate_to_c3d(global_env)

    print(generator.generate_code())


if __name__ == "__main__":
    main()
