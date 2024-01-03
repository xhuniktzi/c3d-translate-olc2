from grammar_opt.lexer import lexer
from grammar_opt.parser import parser
from optimizer.program import Program


def main():
    with open("src/main.c", "r") as f:
        ast: Program = parser.parse(f.read())
        print(ast)


if __name__ == "__main__":
    main()
