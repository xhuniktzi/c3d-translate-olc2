from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.expression import Expression


class AndExpr(Expression):
    def __init__(self, left: Expression, right: Expression):
        super().__init__()
        self.left: Expression = left
        self.right: Expression = right

    def translate_to_c3d(self) -> C3DValue:
        pass
