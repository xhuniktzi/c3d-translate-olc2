from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.expression import Expression
from compiler.expr.finals.enum_datatypes import DataTypes


class Sub(Expression):
    def __init__(self, left: Expression, right: Expression):
        super().__init__()
        self.left: Expression = left
        self.right: Expression = right


def translate_to_c3d(self) -> C3DValue:
    temp_var: str = self.generator.mk_temp()

    left_eval: C3DValue = self.left.translate_to_c3d()
    right_eval: C3DValue = self.right.translate_to_c3d()

    if left_eval.datatype == DataTypes.ENTERO:
        if (
            right_eval.datatype == DataTypes.ENTERO
            or right_eval.datatype == DataTypes.DECIMAL
        ):
            self.generator.register_c3d_expression(
                f"{temp_var} = {left_eval.value} - {right_eval.value}"
            )
            return C3DValue(temp_var, True, DataTypes.ENTERO)

    elif left_eval.datatype == DataTypes.DECIMAL:
        if (
            right_eval.datatype == DataTypes.ENTERO
            or right_eval.datatype == DataTypes.DECIMAL
        ):
            self.generator.register_c3d_expression(
                f"{temp_var} = {left_eval.value} - {right_eval.value}"
            )
            return C3DValue(temp_var, True, DataTypes.DECIMAL)
