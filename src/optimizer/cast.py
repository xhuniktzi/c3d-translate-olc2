from optimizer.i_expr import IExpression


class Cast(IExpression):
    def __init__(self, data_type: str,expr: IExpression) -> None:
        self.expr: IExpression = expr
        self.data_type: str = data_type