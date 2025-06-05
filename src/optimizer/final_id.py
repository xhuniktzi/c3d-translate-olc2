from optimizer.i_expr import IExpression


class FinalId(IExpression):
    def __init__(self, var_id: str) -> None:
        self.var_id: str = var_id