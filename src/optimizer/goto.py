from optimizer.i_statement import IStatement


class Goto(IStatement):
    def __init__(self, label: str) -> None:
        self.label: str = label