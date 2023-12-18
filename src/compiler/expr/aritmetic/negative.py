from compiler.abstract.c3d_symbol import C3DSymbol
from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.expr.finals.enum_datatypes import DataTypes


class Negative(Expression):
    def __init__(self, value: Expression):
        super().__init__()
        self.value: Expression = value

    def translate_to_c3d(self, env: Environment) -> C3DValue:
        temp_var: str = self.generator.mk_temp()

        value_eval: C3DValue = self.value.translate_to_c3d(env)

        value_eval = self.handle_variable(value_eval, env)

        if value_eval.datatype == DataTypes.ENTERO:
            self.generator.register_c3d_expression(temp_var, 0, "-", value_eval.value)
            return C3DValue(temp_var, True, DataTypes.ENTERO)
        elif value_eval.datatype == DataTypes.DECIMAL:
            self.generator.register_c3d_expression(temp_var, 0, "-", value_eval.value)
            return C3DValue(temp_var, True, DataTypes.DECIMAL)

    def handle_variable(self, eval_var: C3DValue, env: Environment) -> C3DValue:
        if eval_var.datatype != DataTypes.IDVARIABLE:
            return eval_var
        else:
            symbol: C3DSymbol = env.get_variable(eval_var.value)
            if symbol is not None:
                temp_var: str = self.generator.mk_temp()
                stack_var: str = self.generator.mk_temp()

                self.generator.access_stack(stack_var, symbol.position)
                self.generator.register_read_stack(temp_var, stack_var)

                return C3DValue(temp_var, True, symbol.datatype)
