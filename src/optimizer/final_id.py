from optimizer.i_expr import IExpression


class FinalId(IExpression):
    def __init__(self, expr: str) -> None:
        self.expr: str = expr