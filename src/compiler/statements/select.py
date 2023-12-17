from compiler.abstract.expression import Expression
from compiler.abstract.statement import Statement


class Select(Statement):
    def __init__(self, expr: Expression):
        super().__init__()
        self.expr: Expression = expr

    def translate_to_c3d(self):
        pass
