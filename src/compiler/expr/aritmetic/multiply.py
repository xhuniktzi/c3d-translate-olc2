from compiler.abstract.expression import Expression


class Multiply(Expression):
    def __init__(self, left, right):
        self.left: Expression = left
        self.right: Expression = right

    def translate_to_c3d(self):
        pass
