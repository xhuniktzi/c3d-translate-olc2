from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """

DECLARE @diasmora AS INT;
SET @diasmora = 45;

	DECLARE @alturamora AS INT;		
    IF (@diasmora > 0 && @diasmora < 30) 
    BEGIN
        SET @alturamora = 0;
    END

    IF (@diasmora >= 30 && @diasmora < 60) 
    BEGIN 
        SET @alturamora = 1;	
    END

    IF (@diasmora >= 30 && @diasmora < 60) 
    BEGIN 
        SET @alturamora = 2;				
    END

    IF (@diasmora >= 60 && @diasmora < 90) 
    BEGIN 
        SET @alturamora = 3;		
    END

    IF (@diasmora >= 90 && @diasmora < 120) 
    BEGIN 
        SET @alturamora = 4;				
    END

SELECT @alturamora;


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
        statement.translate_to_c3d(global_env)

    print(generator.generate_code())


if __name__ == "__main__":
    main()
