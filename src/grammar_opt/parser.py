from optimizer.aritmetic import Aritmetic
from optimizer.array_access import ArrayAccess
from optimizer.array_assign import ArrayAssign
from optimizer.assign import Assign
from optimizer.call import Call
from optimizer.cast import Cast
from optimizer.final_id import FinalId
from optimizer.final_number import FinalNumber
from optimizer.goto import Goto
from optimizer.if_goto import IfGoto
from optimizer.label import Label
from optimizer.logical import Logical
from optimizer.negative import Negative
from optimizer.printf import Printf
from optimizer.ret import Ret
from optimizer.program import Program
import ply.yacc as yacc
from grammar_opt.lexer import tokens

precedence = (
    (
        "nonassoc",
        "EQUALS",
        "NOTEQUALS",
        "GREATER",
        "LESS",
        "GREATEREQUAL",
        "LESSEQUAL",
    ),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("nonassoc", "LPAREN", "RPAREN"),
    ("nonassoc", "NEGATIVE"),
)


# Reglas de producción
def p_program(p):
    """program : includes arrays_def pointers temporals functions main
    | includes arrays_def pointers temporals main"""
    if len(p) == 7:
        p[0] = Program(p[4], p[5], p[6])
    else:
        p[0] = Program(p[4], {}, p[5])

# -- NO SEMANTIC ACTIONS -- #
def p_includes(p):
    """includes : includes include
    | include"""


def p_include(p):
    """include : INCLUDE STDIO_H
    | INCLUDE MATH_H"""


def p_arrays_def(p):
    """arrays_def : arrays_def array_def
    | array_def"""


def p_array_def(p):
    """array_def : DOUBLE ID LBRACKET NUMBER RBRACKET SEMICOLON"""


def p_pointers(p):
    """pointers : pointers pointer
    | pointer"""


def p_pointer(p):
    """pointer : DOUBLE ID ASSIGN NUMBER SEMICOLON"""

# -- SEMANTIC ACTIONS -- #

def p_temporals(p):
    """temporals : DOUBLE list_temporals SEMICOLON"""
    p[0] = p[2]

def p_list_temporals(p):
    """list_temporals : list_temporals COMMA ID
    | ID"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_functions(p):
    """functions : functions function
    | function"""
    if len(p) == 3:
        p[0] = {**p[1], **p[2]}
    else:
        p[0] = p[1]


def p_function(p):
    """function : VOID ID LPAREN RPAREN LBRACE body RBRACE"""
    p[0] = {p[2]: p[6]}


def p_main(p):
    """main : INT MAIN LPAREN RPAREN LBRACE body RBRACE"""
    p[0] = p[6]


def p_body(p):
    """body : body statement
    | statement"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_statement(p):
    """statement : return
    | assignment
    | if_goto
    | goto
    | label
    | print
    | array_assign
    | call
    """
    p[0] = p[1]


def p_return(p):
    """return : RET expression SEMICOLON
    | RET SEMICOLON"""
    if len(p) == 4:
        p[0] = Ret(p[2])
    else:
        p[0] = Ret()


def p_assignment(p):
    """assignment : ID ASSIGN expression SEMICOLON"""
    p[0] = Assign(p[1] ,p[3])


def p_if_goto(p):
    """if_goto : IF LPAREN expression RPAREN GOTO ID SEMICOLON"""
    p[0] = IfGoto(p[3], p[6])


def p_goto(p):
    """goto : GOTO ID SEMICOLON"""
    p[0] = Goto(p[2])

def p_label(p):
    """label : ID COLON"""
    p[0] = Label(p[1])


def p_print(p):
    """print : PRINTF LPAREN STRING COMMA expression RPAREN SEMICOLON"""
    p[0] = Printf(p[3], p[5])


def p_array_assign(p):
    """array_assign : ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON"""
    p[0] = ArrayAssign(p[1], p[3], p[6])

def p_call(p):
    """call : ID LPAREN RPAREN SEMICOLON"""
    p[0] = Call(p[1])


def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = FinalNumber(p[1])


def p_expression_id(p):
    """expression : ID"""
    p[0] = FinalId(p[1])


def p_expression_cast(p):
    """expression : LPAREN INT RPAREN expression
    | LPAREN DOUBLE RPAREN expression"""
    p[0] = Cast(p[2], p[4])


def p_expression_array_access(p):
    """expression : ID LBRACKET expression RBRACKET"""
    p[0] = ArrayAccess(p[1], p[3])


def p_expression_logical(p):
    """expression : expression EQUALS expression
    | expression NOTEQUALS expression
    | expression GREATER expression
    | expression LESS expression
    | expression GREATEREQUAL expression
    | expression LESSEQUAL expression"""
    p[0] = Logical(p[1], p[2], p[3])

def p_expression_arithmetic(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression"""
    p[0] = Aritmetic(p[1], p[2], p[3])

def p_expression_unop(p):
    """expression : MINUS expression %prec NEGATIVE"""
    p[0] = Negative(p[2])

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


parser = yacc.yacc()
