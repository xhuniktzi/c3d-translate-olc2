from optimizer.i_statement import IStatement


class Call(IStatement):
    def __init__(self, name: str) -> None:
        self.name: str = name
   