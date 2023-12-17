from compiler.abstract.expression import Expression


class Negative(Expression):
    def __init__(self, value: Expression):
        super().__init__()
        self.value: Expression = value

    def translate_to_c3d(self):
        pass
