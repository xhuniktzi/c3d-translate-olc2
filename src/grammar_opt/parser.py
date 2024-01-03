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


def p_temporals(p):
    """temporals : DOUBLE list_temporals SEMICOLON"""


def p_list_temporals(p):
    """list_temporals : list_temporals COMMA ID
    | ID"""


def p_functions(p):
    """functions : functions function
    | function"""


def p_function(p):
    """function : VOID ID LPAREN RPAREN LBRACE body RBRACE"""


def p_main(p):
    """main : INT MAIN LPAREN RPAREN LBRACE body RBRACE"""


def p_body(p):
    """body : body statement
    | statement"""


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


def p_return(p):
    """return : RET expression SEMICOLON
    | RET SEMICOLON"""


def p_assignment(p):
    """assignment : ID ASSIGN expression SEMICOLON"""


def p_if_goto(p):
    """if_goto : IF LPAREN expression RPAREN GOTO ID SEMICOLON"""


def p_goto(p):
    """goto : GOTO ID SEMICOLON"""


def p_label(p):
    """label : ID COLON"""


def p_print(p):
    """print : PRINTF LPAREN STRING COMMA expression RPAREN SEMICOLON"""


def p_array_assign(p):
    """array_assign : ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON"""

def p_call(p):
    """call : ID LPAREN RPAREN SEMICOLON"""


def p_expression_number(p):
    """expression : NUMBER"""


def p_expression_id(p):
    """expression : ID"""


def p_expression_cast(p):
    """expression : LPAREN INT RPAREN expression
    | LPAREN DOUBLE RPAREN expression"""


def p_expression_array_access(p):
    """expression : ID LBRACKET expression RBRACKET"""


def p_expression_binop(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | expression EQUALS expression
    | expression NOTEQUALS expression
    | expression GREATER expression
    | expression LESS expression
    | expression GREATEREQUAL expression
    | expression LESSEQUAL expression"""

def p_expression_unop(p):
    """expression : MINUS expression %prec NEGATIVE"""

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


parser = yacc.yacc()
