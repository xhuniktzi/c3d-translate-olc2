from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.expr.finals.enum_datatypes import DataTypes


class Minor(Expression):
    def __init__(self, left: Expression, right: Expression):
        super().__init__()
        self.left: Expression = left
        self.right: Expression = right

    def translate_to_c3d(self, env: Environment) -> C3DValue:
        true_label: str = self.generator.mk_label()
        false_label: str = self.generator.mk_label()

        left_value: C3DValue = self.left.translate_to_c3d(env)
        right_value: C3DValue = self.right.translate_to_c3d(env)

        self.generator.register_if_goto(
            left_value.value, "<", right_value.value, true_label
        )
        self.generator.register_goto(false_label)

        return C3DValue(None, False, DataTypes.BOOLEAN, true_label, false_label)
