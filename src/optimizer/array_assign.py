from optimizer.i_expr import IExpression
from optimizer.i_statement import IStatement


class ArrayAssign(IStatement):
    def __init__(self, target: str, index: IExpression, expr: IExpression) -> None:
        self.target: str = target
        self.index: IExpression = index
        self.expr: IExpression = expr