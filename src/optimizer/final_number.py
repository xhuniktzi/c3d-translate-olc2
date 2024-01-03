from optimizer.i_expr import IExpression


class FinalNumber(IExpression):
    def __init__(self, expr: float) -> None:
        self.expr: float = expr