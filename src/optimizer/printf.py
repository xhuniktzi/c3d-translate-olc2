from optimizer.i_expr import IExpression
from optimizer.i_statement import IStatement


class Printf(IStatement):
    def __init__ (self, control: str, expr: IExpression) -> None:
        self.control: str = control
        self.expr: IExpression = expr