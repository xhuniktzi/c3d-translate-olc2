from compiler.abstract.expression import Expression


class Param:
    def __init__(self, id_var: str, expr: Expression) -> None:
        self.id_var: str = id_var
        self.expr: Expression = expr
