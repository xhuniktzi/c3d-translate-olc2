from optimizer.i_expr import IExpression


class Logical(IExpression):
    def __init__(self, left: IExpression, operator: str, right: IExpression) -> None:
        self.left: IExpression = left
        self.operator: str = operator
        self.right: IExpression = right