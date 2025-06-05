from optimizer.i_expr import IExpression
from optimizer.i_statement import IStatement


class Ret(IStatement):
    def __init__(self, expr: IExpression = None) -> None:
        self.expr: IExpression = expr