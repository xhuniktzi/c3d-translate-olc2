import ply.lex as lex

reserved = {
    "if": "IF",
    "goto": "GOTO",
    "return": "RET",
    "printf": "PRINTF",
    "main": "MAIN",

    "double": "DOUBLE",
    "int": "INT",
    "void": "VOID",
}
# Lista de tokens
tokens = (
    "ID",
    "INCLUDE",
    "STDIO_H",
    "MATH_H",
    "NUMBER",
    "STRING",
    "SEMICOLON",
    "COLON",
    "COMMA",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "LBRACKET",
    "RBRACKET",
    "ASSIGN",
    "EQUALS",
    "NOTEQUALS",
    "GREATER",
    "LESS",
    "GREATEREQUAL",
    "LESSEQUAL",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
)

tokens = tokens + tuple(reserved.values())

# Reglas para tokens simples
t_SEMICOLON = r"\;"
t_COLON = r"\:"
t_COMMA = r"\,"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_ASSIGN = r"\="
t_EQUALS = r"\=\="
t_NOTEQUALS = r"\!\="
t_GREATER = r"\>"
t_LESS = r"\<"
t_GREATEREQUAL = r"\>\="
t_LESSEQUAL = r"\<\="
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"



def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value.lower(), "ID")
    return t

def t_INCLUDE(t):
    r"\#include"
    return t

def t_STDIO_H(t):
    r"<stdio.h>"
    return t

def t_MATH_H(t):
    r"<math.h>"
    return t

def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = float(t.value)
    return t


def t_STRING(t):
    r"\".*?\" "
    return t


# Ignorar espacios y tabulaciones
t_ignore = " \t\n\r"


# Manejo de errores
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# Construir el lexer
lexer = lex.lex()
