from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.expression import Expression
from compiler.expr.finals.enum_datatypes import DataTypes


class Negative(Expression):
    def __init__(self, value: Expression):
        super().__init__()
        self.value: Expression = value

    def translate_to_c3d(self) -> C3DValue:
        temp_var: str = self.generator.mk_temp()

        value_eval: C3DValue = self.value.translate_to_c3d()

        if value_eval.datatype == DataTypes.ENTERO:
            self.generator.register_c3d_expression(
                f"{temp_var} = 0 - {value_eval.value}"
            )
            return C3DValue(temp_var, True, DataTypes.ENTERO)
        elif value_eval.datatype == DataTypes.DECIMAL:
            self.generator.register_c3d_expression(
                f"{temp_var} = 0 - {value_eval.value}"
            )
            return C3DValue(temp_var, True, DataTypes.DECIMAL)
