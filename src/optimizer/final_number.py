from optimizer.i_expr import IExpression


class FinalNumber(IExpression):
    def __init__(self, final_number: float) -> None:
        self.final_number: float = final_number