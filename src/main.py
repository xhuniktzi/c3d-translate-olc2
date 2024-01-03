from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """
    CREATE FUNCTION fn_retornaalturamora (@diasmora int)
RETURN nvarchar
AS
BEGIN
	DECLARE @alturamora AS nvarchar;

		IF (@diasmora > 0 && @diasmora < 30) 
		BEGIN
			SET @alturamora = 'Al dia';
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 'Altura Mora 2';	
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 'Altura Mora 3';				
		END;

		IF (@diasmora >= 60 && @diasmora < 90) 
		BEGIN 
			SET @alturamora = 'Altura Mora 4';		
		END;
	
		IF (@diasmora >= 90 && @diasmora < 120) 
		BEGIN 
			SET @alturamora = 'Altura Mora 5';				
		END;

		
	RETURN @alturamora;

END;

    
    CREATE PROCEDURE sp_actualizaalturamora (@credito int,@diasmora int)
AS
BEGIN
	DECLARE @alturamora AS int;

		IF (@diasmora > 0 && @diasmora < 30) 
		BEGIN
			SET @alturamora = 0;
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 1;	
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 2;				
		END;

		IF (@diasmora >= 60 && @diasmora < 90) 
		BEGIN 
			SET @alturamora = 3;		
		END;
	
		IF (@diasmora >= 90 && @diasmora < 120) 
		BEGIN 
			SET @alturamora = 4;				
		END;

		             
		SELECT @alturamora;
END;
    
CREATE FUNCTION sp_calculacuota (@saldo decimal, @plazo int ,@diasmora int)
RETURN decimal
AS
BEGIN
		DECLARE @cuota as decimal;
		DECLARE @ajuste as decimal;
		
		IF (@saldo > 5000 && @diasmora > 30)
		begin 
			set @cuota = (@saldo/@plazo)*0.45;
		END;
	
		if (@saldo > 15000 && @diasmora > 30) 
		BEGIN
			set @cuota = (@saldo/@plazo)*0.65;	
		END;

		if (@saldo > 25000 && @diasmora > 60) 
		BEGIN
			set @cuota = (@saldo/@plazo)*0.70;			
		END;
	
		if (@saldo < 15000 && @diasmora < 30) 
		BEGIN
			set @cuota = (@saldo/@plazo)*0.15;			
		END;

        IF (@cuota > 1000 && @cuota < 1500)
        BEGIN 
            SET @ajuste = 75;
        END
        ELSE 
        BEGIN 
            IF (@cuota >= 1500 && @cuota < 2000)
            BEGIN 
                SET @ajuste = 125;
            END
            ELSE 
            BEGIN 
                IF (@cuota > 0 && @cuota < 1000)
                BEGIN 
                    SET @ajuste = 25;
                END
                ELSE 
                BEGIN 
                    IF (@cuota >= 2000)
                    BEGIN 
                        SET @ajuste = 150;
                    END
                    ELSE 
                    BEGIN 
                        SET @ajuste = 0;
                    END;
                END;
            END;
        END;

		
		SET @cuota = @cuota-@ajuste;	
			
		RETURN @cuota;	
		
		
END;

	SELECT sp_calculacuota(@saldo = 4000, @plazo = 10, @diasmora = 20);
	SELECT sp_calculacuota(@saldo = 10000, @plazo = 10, @diasmora = 40);
	EXEC sp_actualizaalturamora(@credito = 1,@diasmora = 10);
	EXEC sp_actualizaalturamora(@credito = 2,@diasmora = 40);
    
    SELECT fn_retornaalturamora(@diasmora = 10);
	SELECT fn_retornaalturamora(@diasmora = 40);
    
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
