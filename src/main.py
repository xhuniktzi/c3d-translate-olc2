from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from compiler.statements.define_procedure import DefineProcedure
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """

CREATE PROCEDURE sp_actualizaalturamora (@credito int,@diasmora int)
AS
BEGIN
	DECLARE @alturamora AS int;	
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
END

DECLARE @credito AS int;
SET @credito = 1;
EXEC sp_actualizaalturamora (@credito = @credito, @diasmora = 2);
EXEC sp_actualizaalturamora (@credito = @credito, @diasmora = 30);
EXEC sp_actualizaalturamora (@credito =@credito, @diasmora = 60);
EXEC sp_actualizaalturamora (@credito =@credito, @diasmora = 90);
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
