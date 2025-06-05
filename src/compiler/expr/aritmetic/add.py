from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        super().__init__()
        self.left: Expression = left
        self.right: Expression = right

    def translate_to_c3d(self, env: Environment) -> C3DValue:
        left: C3DValue = self.left.translate_to_c3d(env)
        right: C3DValue = self.right.translate_to_c3d(env)

        self.data_type = left.data_type

        generator: Generator = Generator(env)

        if left.data_type == DataTypes.STRING and right.data_type == DataTypes.INT:
            generator = left.generator.combine(right.generator)
            temp_var: str = generator.te
