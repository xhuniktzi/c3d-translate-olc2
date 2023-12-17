import ply.yacc as yacc
from grammar.lexer import tokens

precedence = (
    ("left", "OR", "AND"),
    ("right", "NUMERONEGATIVO"),
    ("left", "IGUALLOGICO", "DIFERENTE", "MENOR", "MENORIGUAL", "MAYOR", "MAYORIGUAL"),
    ("left", "SUMA", "RESTA"),
    ("left", "MULTIPLICACION", "DIVISION"),
    ("left", "PARENTESISABRE", "PARENTESISCIERRA"),
)


def p_program(p):
    """program : statements"""


def p_statements(p):
    """statements : statements statement
    | statement"""


def p_statement(p):
    """statement : declaracion
    | asignacion
    | condicion
    | ciclo
    | procedure
    | llamada
    | select"""


def p_declare(p):
    """declaracion : DECLARE IDVARIABLE AS TIPODATO PUNTOYCOMA"""


def p_asignacion(p):
    """asignacion : SET IDVARIABLE IGUAL expresion PUNTOYCOMA"""


def p_select(p):
    """select : SELECT expresion PUNTOYCOMA"""


def p_condicion(p):
    """condicion : IF  PARENTESISABRE expresion PARENTESISCIERRA BEGIN statements END
    | IF  PARENTESISABRE expresion PARENTESISCIERRA BEGIN statements END ELSE BEGIN statements END
    """


def p_ciclo(p):
    """ciclo : WHILE PARENTESISABRE expresion PARENTESISCIERRA BEGIN statements END"""


def p_procedure(p):
    """procedure : CREATE PROCEDURE IDENTIFICADORGLOBAL PARENTESISABRE args_list PARENTESISCIERRA BEGIN statements END"""


def p_llamada(p):
    """llamada : EXEC IDENTIFICADORGLOBAL PARENTESISABRE params_list PARENTESISCIERRA PUNTOYCOMA"""


def p_args_list(p):
    """args_list : args_list COMA IDVARIABLE TIPODATO
    | IDVARIABLE TIPODATO"""


def p_params_list(p):
    """params_list : params_list COMA IDVARIABLE IGUAL expresion
    | IDVARIABLE IGUAL expresion"""


def p_expresion_relacionales(p):
    """expresion : relacionales"""


def p_expresion_logicas(p):
    """expresion : logicas"""


def p_expresion_valoresfinales(p):
    """expresion : valoresfinales"""


def p_expresion_aritmeticas(p):
    """expresion : aritmeticas"""


def p_expresion_null(p):
    """expresion : NULL"""


def p_expresion_parentesis(p):
    """expresion : PARENTESISABRE expresion PARENTESISCIERRA"""


def p_valoresfinales_numeroflotante(p):
    """valoresfinales : DECIMAL"""


def p_valoresfinales_cadena(p):
    """valoresfinales : CADENA"""


def p_valoresfinales_idvariable(p):
    """valoresfinales : IDVARIABLE"""


def p_valoresfinales_numero(p):
    """valoresfinales : ENTERO"""


def p_relacionales_mayor(p):
    """relacionales : expresion MAYOR expresion"""


def p_relacionales_menor(p):
    """relacionales : expresion MENOR expresion"""


def p_relacionales_mayorigual(p):
    """relacionales : expresion MAYORIGUAL expresion"""


def p_relacionales_menorigual(p):
    """relacionales : expresion MENORIGUAL expresion"""


def p_relacionales_igual(p):
    """relacionales : expresion IGUALLOGICO expresion"""


def p_relacionales_diferente(p):
    """relacionales : expresion DIFERENTE expresion"""


def p_logicas_and(p):
    """logicas : expresion AND expresion"""


def p_logicas_or(p):
    """logicas : expresion OR expresion"""


def p_aritmeticas_numeronegativo(p):
    """aritmeticas : RESTA expresion %prec NUMERONEGATIVO"""


def p_aritmeticas_suma(p):
    """aritmeticas : expresion SUMA expresion"""


def p_aritmeticas_resta(p):
    """aritmeticas : expresion RESTA expresion"""


def p_aritmeticas_multiplicacion(p):
    """aritmeticas : expresion MULTIPLICACION expresion"""


def p_aritmeticas_division(p):
    """aritmeticas : expresion DIVISION expresion"""


def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()
