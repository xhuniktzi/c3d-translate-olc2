from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """
    DECLARE @a AS DECIMAL;
    DECLARE @b AS INT;
    DECLARE @c AS NVARCHAR;
    DECLARE @d AS NVARCHAR;

    SET @a = 5*4-3+10-11/3*21/13;
    SET @b = 13-4*43/2+1;
    SET @c = "Hola mundo soy yo";
    SET @d = "Hola mundo soy yo y quiero probar algo";
    
    SELECT @a;
    SELECT @b;

    SELECT "Hola mundo";
    SELECT @c;
    SELECT @d;
    SELECT "Debo probar todos los casos";
    
    SELECT 123.456;
    SELECT 123;

    SELECT @a + @b;
    SELECT 70 + @b;
    SELECT @b + 70;
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
