from optimizer.i_expr import IExpression


class Negative(IExpression):
    def __init__(self, expr: IExpression) -> None:
        self.expr: IExpression = expr