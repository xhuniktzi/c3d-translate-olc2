from grammar_opt.lexer import lexer
from grammar_opt.parser import parser


def main():
    with open("src/main.c", "r") as f:
        parser.parse(f.read())


if __name__ == "__main__":
    main()
