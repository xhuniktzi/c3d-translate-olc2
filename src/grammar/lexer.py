import ply.lex as lex


# reserved words
reserved = {
    "create": "CREATE",
    "procedure": "PROCEDURE",
    "as": "AS",
    "begin": "BEGIN",
    "declare": "DECLARE",
    "if": "IF",
    "while": "WHILE",
    "select": "SELECT",
    "set": "SET",
    "else": "ELSE",
    "end": "END",
    "null": "NULL",
    "int": "TIPODATO",
    "decimal": "TIPODATO",
    "nvarchar": "TIPODATO",
    "exec": "EXEC",
}

# tokens
tokens = (
    "IDVARIABLE",
    "PUNTOYCOMA",
    "COMA",
    "CADENA",
    "IGUAL",
    "SUMA",
    "RESTA",
    "MULTIPLICACION",
    "DIVISION",
    "IGUALLOGICO",
    "DIFERENTE",
    "MENOR",
    "MAYOR",
    "MENORIGUAL",
    "MAYORIGUAL",
    "OR",
    "AND",
    "PARENTESISABRE",
    "PARENTESISCIERRA",
    "DECIMAL",
    "ENTERO",
    "IDENTIFICADORGLOBAL",
)

tokens = tokens + tuple(reserved.values())

# Regular expressions rules for a simple tokens
t_IDVARIABLE = r"@[a-zA-Z_][a-zA-Z0-9_]*"
t_PUNTOYCOMA = r";"
t_COMA = r","
t_CADENA = r"\".*?\""


t_IGUAL = r"="

t_SUMA = r"\+"
t_RESTA = r"-"
t_MULTIPLICACION = r"\*"
t_DIVISION = r"/"

t_IGUALLOGICO = r"=="
t_DIFERENTE = r"!="
t_MENOR = r"<"
t_MAYOR = r">"
t_MENORIGUAL = r"<="
t_MAYORIGUAL = r">="

t_OR = r"\|\|"
t_AND = r"&&"

t_PARENTESISABRE = r"\("
t_PARENTESISCIERRA = r"\)"

t_ignore = " \t\n\r"


## DECIMAL
def t_DECIMAL(t):
    r"\d+\.\d+"
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error en los Flotantes %d", t.value)
        t.value = 0
    return t


## ENTEROS
def t_ENTERO(t):
    r"\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Error en el Entero Esperado %d", t.value)
        t.value = 0
    return t


# Regla para palabras reservadas e identificadores
def t_IDENTIFICADORGLOBAL(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value.lower(), "IDENTIFICADORGLOBAL")
    return t


## Error handling rule
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
