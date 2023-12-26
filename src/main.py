from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """
CREATE FUNCTION fn_retornaalturamora (@diasmora INT)
RETURN NVARCHAR
AS
BEGIN
	    DECLARE @alturamora AS NVARCHAR;

		IF (@diasmora > 0 && @diasmora < 30) 
		BEGIN
			SET @alturamora = "Al dia";
		END
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = "Altura Mora 2";	
		END
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = "Altura Mora 3";				
		END

		IF (@diasmora >= 60 && @diasmora < 90) 
		BEGIN 
			SET @alturamora = "Altura Mora 4";		
		END
	
		IF (@diasmora >= 90 && @diasmora < 120) 
		BEGIN 
			SET @alturamora = "Altura Mora 5";				
		END
 
		
	RETURN @alturamora;

END

CREATE PROCEDURE sp_actualizaalturamora (@credito INT,@diasmora INT)
AS
BEGIN
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
END

CREATE FUNCTION sp_calculacuota (@saldo DECIMAL, @plazo int ,@diasmora int)
RETURN DECIMAL
AS
BEGIN
		DECLARE @cuota AS DECIMAL;
		DECLARE @ajuste AS DECIMAL; 
		
		IF (@saldo > 5000 && @diasmora > 30)
		begin 
			SET @cuota = (@saldo/@plazo)*0.45;
		END
	
		IF (@saldo > 15000 && @diasmora > 30) 
		BEGIN
			SET @cuota = (@saldo/@plazo)*0.65;	
		END

		IF (@saldo > 25000 && @diasmora > 60) 
		BEGIN
			SET @cuota = (@saldo/@plazo)*0.70;			
		END
	
		IF (@saldo < 15000 && @diasmora < 30) 
		BEGIN
			SET @cuota = (@saldo/@plazo)*0.15;			
		END
	
		IF( @cuota > 1000 && @cuota <  1500)
        BEGIN
			SET @ajuste = 75;
		END
        
        IF (@cuota >= 1500 && @cuota <  2000)
        BEGIN
            SET @ajuste = 125;
        END

        IF ( @cuota > 0 &&  @cuota < 1000)
        BEGIN
             SET @ajuste = 25;
        END
    
        IF ( @cuota >=  2000)
        BEGIN
            SET @ajuste = 150;
        END				
        ELSE
        BEGIN
             SET @ajuste = 0;
        END
		
		SET @cuota = @cuota-@ajuste;	
			
		RETURN @cuota;	
		
		
END

SELECT fn_retornaalturamora(@diasmora = 10);
SELECT fn_retornaalturamora(@diasmora = 40);
SELECT fn_retornaalturamora(@diasmora = 70);
SELECT fn_retornaalturamora(@diasmora = 100);

EXEC sp_actualizaalturamora(@credito = 1,@diasmora = 10);
EXEC sp_actualizaalturamora(@credito = 2,@diasmora = 40);
EXEC sp_actualizaalturamora(@credito = 3,@diasmora = 70);
EXEC sp_actualizaalturamora(@credito = 4,@diasmora = 100);

SELECT sp_calculacuota(@saldo = 10000,@plazo = 12,@diasmora = 10);
SELECT sp_calculacuota(@saldo = 20000,@plazo = 12,@diasmora = 40);
SELECT sp_calculacuota(@saldo = 30000,@plazo = 12,@diasmora = 70);
SELECT sp_calculacuota(@saldo = 40000,@plazo = 12,@diasmora = 100);

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
