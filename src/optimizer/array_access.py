from optimizer.i_expr import IExpression


class ArrayAccess(IExpression):
    def __init__(self, target: str, index: IExpression) -> None:
        self.target: str = target
        self.index: IExpression = index