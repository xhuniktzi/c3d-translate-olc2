from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class Negative(Expression):
    def __init__(self, value: Expression):
        super().__init__()
        self.value: Expression = value

    def translate_to_c3d(self, env: Environment) -> C3DValue:
        pass
