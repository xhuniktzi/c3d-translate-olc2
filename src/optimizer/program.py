from optimizer.i_statement import IStatement


class Program:
    def __init__(self, temporals: list[str], functions: dict[str, list[IStatement]], main: list[IStatement]) -> None:
        self.temporals: list[str] = temporals
        self.functions: dict[str, list[IStatement]] = functions
        self.main: list[IStatement] = main