from compiler.expr.aritmetic.div import Div
from compiler.expr.aritmetic.multiply import Multiply
from compiler.expr.aritmetic.add import Add
from compiler.expr.aritmetic.negative import Negative
from compiler.expr.aritmetic.sub import Sub
from compiler.expr.finals.call_function import CallFunction
from compiler.expr.finals.enum_datatypes import DataTypes
from compiler.expr.finals.term_value import TermValue
from compiler.expr.logical.and_expr import AndExpr
from compiler.expr.logical.or_expr import OrExpr
from compiler.expr.relationals.equals import Equals
from compiler.expr.relationals.major import Major
from compiler.expr.relationals.majorequals import MajorEquals
from compiler.expr.relationals.minor import Minor
from compiler.expr.relationals.minorequals import MinorEquals
from compiler.expr.relationals.notequals import NotEquals
from compiler.expr.transport.args import Args
from compiler.expr.transport.param import Param
from compiler.helpers.str_to_datatype import fnStrToDatatype
from compiler.statements.assign import Assign
from compiler.statements.call_procedure import CallProcedure
from compiler.statements.declare import Declare
from compiler.statements.define_function import DefineFunction
from compiler.statements.define_procedure import DefineProcedure
from compiler.statements.if_statement import IfStatement
from compiler.statements.return_statement import ReturnStatement
from compiler.statements.select import Select
from compiler.statements.while_statement import WhileStatement
import ply.yacc as yacc
from grammar.lexer import tokens


precedence = (
    ("left", "OR"),
    ("left", "AND"),
    (
        "nonassoc",
        "IGUALLOGICO",
        "DIFERENTE",
        "MENOR",
        "MENORIGUAL",
        "MAYOR",
        "MAYORIGUAL",
    ),
    ("left", "SUMA", "RESTA"),
    ("left", "MULTIPLICACION", "DIVISION"),
    ("nonassoc", "PARENTESISABRE", "PARENTESISCIERRA"),
    ("nonassoc", "NUMERONEGATIVO"),
)


def p_program(p):
    """program : statements"""
    p[0] = p[1]


def p_statements(p):
    """statements : statements statement
    | statement"""
    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = []
        p[0].append(p[1])


def p_statement(p):
    """statement : declaracion
    | asignacion
    | select
    | condicion
    | procedure
    | llamada
    | function
    | return
    | ciclo
    """
    p[0] = p[1]


def p_declare(p):
    """declaracion : DECLARE IDVARIABLE AS TIPODATO PUNTOYCOMA"""
    p[0] = Declare(p[2], fnStrToDatatype(p[4]))


def p_asignacion(p):
    """asignacion : SET IDVARIABLE IGUAL expresion PUNTOYCOMA"""
    p[0] = Assign(p[2], p[4])


def p_select(p):
    """select : SELECT expresion PUNTOYCOMA"""
    p[0] = Select(p[2])


def p_condicion(p):
    """condicion : IF  PARENTESISABRE expresion PARENTESISCIERRA BEGIN statements END PUNTOYCOMA
    | IF  PARENTESISABRE expresion PARENTESISCIERRA BEGIN statements END ELSE BEGIN statements END PUNTOYCOMA
    """
    if len(p) == 9:
        p[0] = IfStatement(p[3], p[6])
    else:
        p[0] = IfStatement(p[3], p[6], p[10])


def p_return(p):
    """return : RETURN expresion PUNTOYCOMA
    | RETURN PUNTOYCOMA"""

    if len(p) == 4:
        p[0] = ReturnStatement(p[2])
    else:
        p[0] = ReturnStatement(None)


def p_ciclo(p):
    """ciclo : WHILE PARENTESISABRE expresion PARENTESISCIERRA BEGIN statements END"""
    p[0] = WhileStatement(p[3], p[6])


def p_procedure(p):
    """procedure : CREATE PROCEDURE IDENTIFICADORGLOBAL PARENTESISABRE args_list PARENTESISCIERRA AS BEGIN statements END PUNTOYCOMA
    | CREATE PROCEDURE IDENTIFICADORGLOBAL PARENTESISABRE PARENTESISCIERRA AS BEGIN statements END PUNTOYCOMA
    """
    if len(p) == 12:
        p[0] = DefineProcedure(p[3], p[5], p[9])
    else:
        p[0] = DefineProcedure(p[3], [], p[7])


def p_function(p):
    """
    function : CREATE FUNCTION IDENTIFICADORGLOBAL PARENTESISABRE args_list PARENTESISCIERRA RETURN TIPODATO AS BEGIN statements END PUNTOYCOMA
    | CREATE FUNCTION IDENTIFICADORGLOBAL PARENTESISABRE PARENTESISCIERRA RETURN TIPODATO AS BEGIN statements END PUNTOYCOMA
    """
    if len(p) == 14:
        p[0] = DefineFunction(p[3], p[5], p[11], fnStrToDatatype(p[8]))
    else:
        p[0] = DefineFunction(p[3], [], p[9], fnStrToDatatype(p[6]))


def p_llamada(p):
    """llamada : EXEC IDENTIFICADORGLOBAL PARENTESISABRE params_list PARENTESISCIERRA PUNTOYCOMA
    | EXEC IDENTIFICADORGLOBAL PARENTESISABRE PARENTESISCIERRA PUNTOYCOMA"""
    if len(p) == 7:
        p[0] = CallProcedure(p[2], p[4])
    else:
        p[0] = CallProcedure(p[2], [])


def p_args_list(p):
    """args_list : args_list COMA IDVARIABLE TIPODATO
    | IDVARIABLE TIPODATO"""
    if len(p) == 5:
        p[0] = p[1]
        p[0].append(Args(p[3], fnStrToDatatype(p[4])))
    else:
        p[0] = []
        p[0].append(Args(p[1], fnStrToDatatype(p[2])))


def p_params_list(p):
    """params_list : params_list COMA IDVARIABLE IGUAL expresion
    | IDVARIABLE IGUAL expresion"""
    if len(p) == 6:
        p[0] = p[1]
        p[0].append(Param(p[3], p[5]))
    else:
        p[0] = []
        p[0].append(Param(p[1], p[3]))


def p_expresion_relacionales(p):
    """expresion : relacionales"""
    p[0] = p[1]


def p_expresion_logicas(p):
    """expresion : logicas"""
    p[0] = p[1]


def p_expresion_valoresfinales(p):
    """expresion : valoresfinales"""
    p[0] = p[1]


def p_expresion_aritmeticas(p):
    """expresion : aritmeticas"""
    p[0] = p[1]


def p_expresion_parentesis(p):
    """expresion : PARENTESISABRE expresion PARENTESISCIERRA"""
    p[0] = p[2]


def p_expresion_funcion(p):
    """expresion : IDENTIFICADORGLOBAL PARENTESISABRE params_list PARENTESISCIERRA"""
    p[0] = CallFunction(p[1], p[3])


def p_valoresfinales_numero(p):
    """valoresfinales : ENTERO"""
    p[0] = TermValue(p[1], DataTypes.ENTERO)


def p_valoresfinales_numeroflotante(p):
    """valoresfinales : DECIMAL"""
    p[0] = TermValue(p[1], DataTypes.DECIMAL)


def p_valoresfinales_cadena(p):
    """valoresfinales : CADENA"""
    p[0] = TermValue(p[1], DataTypes.CADENA)


def p_valoresfinales_idvariable(p):
    """valoresfinales : IDVARIABLE"""
    p[0] = TermValue(p[1], DataTypes.IDVARIABLE)


def p_valoresfinales_booleano(p):
    """valoresfinales : BOOL"""
    p[0] = TermValue(p[1], DataTypes.BOOLEAN)


def p_expresion_null(p):
    """valoresfinales : NULL"""
    p[0] = TermValue(None, DataTypes.NULL)


def p_relacionales_mayor(p):
    """relacionales : expresion MAYOR expresion"""
    p[0] = Major(p[1], p[3])


def p_relacionales_menor(p):
    """relacionales : expresion MENOR expresion"""
    p[0] = Minor(p[1], p[3])


def p_relacionales_mayorigual(p):
    """relacionales : expresion MAYORIGUAL expresion"""
    p[0] = MajorEquals(p[1], p[3])


def p_relacionales_menorigual(p):
    """relacionales : expresion MENORIGUAL expresion"""
    p[0] = MinorEquals(p[1], p[3])


def p_relacionales_igual(p):
    """relacionales : expresion IGUALLOGICO expresion"""
    p[0] = Equals(p[1], p[3])


def p_relacionales_diferente(p):
    """relacionales : expresion DIFERENTE expresion"""
    p[0] = NotEquals(p[1], p[3])


def p_logicas_and(p):
    """logicas : expresion AND expresion"""
    p[0] = AndExpr(p[1], p[3])


def p_logicas_or(p):
    """logicas : expresion OR expresion"""
    p[0] = OrExpr(p[1], p[3])


def p_aritmeticas_numeronegativo(p):
    """aritmeticas : RESTA expresion %prec NUMERONEGATIVO"""
    p[0] = Negative(p[2])


def p_aritmeticas_suma(p):
    """aritmeticas : expresion SUMA expresion"""

    p[0] = Add(p[1], p[3])


def p_aritmeticas_resta(p):
    """aritmeticas : expresion RESTA expresion"""

    p[0] = Sub(p[1], p[3])


def p_aritmeticas_multiplicacion(p):
    """aritmeticas : expresion MULTIPLICACION expresion"""

    p[0] = Multiply(p[1], p[3])


def p_aritmeticas_division(p):
    """aritmeticas : expresion DIVISION expresion"""

    p[0] = Div(p[1], p[3])


def p_error(t):
    # print("Error sintáctico en '%s'" % t.value)
    raise Exception("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()
