from compiler.abstract.Generator import Generator
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from grammar.lexer import lexer
from grammar.parser import parser


def main():
    textoAnalizar: str = """
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
