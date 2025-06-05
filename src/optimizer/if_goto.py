from optimizer.i_expr import IExpression
from optimizer.i_statement import IStatement


class IfGoto(IStatement):
    def __init__(self, condition: IExpression, label: str) -> None:
        self.condition: IExpression = condition
        self.label: str = label