from optimizer.i_expr import IExpression
from optimizer.i_statement import IStatement


class Assign(IStatement):
    def __init__(self, target: str, expr: IExpression) -> None:
        self.target: str = target
        self.expr: IExpression = expr