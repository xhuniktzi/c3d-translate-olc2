from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.abstract.statement import Statement
from compiler.expr.finals.enum_datatypes import DataTypes


class Select(Statement):
    def __init__(self, expr: Expression):
        super().__init__()
        self.expr: Expression = expr

    def translate_to_c3d(self, env: Environment):
        variable_eval: C3DValue = self.expr.translate_to_c3d(env)

        if variable_eval.datatype == DataTypes.ENTERO:
            self.generator.register_C_printf("%d", f"(int){variable_eval.value}")
        elif variable_eval.datatype == DataTypes.IDVARIABLE:
            symbol = env.get_variable(variable_eval.value)
            if symbol is None:
                return

            temp_variable: str = self.generator.mk_temp()
            if symbol.datatype == DataTypes.ENTERO:
                self.generator.register_read_stack(temp_variable, symbol.position)
                self.generator.register_C_printf("%d", f"(int){temp_variable}")
            elif symbol.datatype == DataTypes.DECIMAL:
                self.generator.register_read_stack(temp_variable, symbol.position)
                self.generator.register_C_printf("%f", f"(double){temp_variable}")
            elif symbol.datatype == DataTypes.CADENA:
                self.generator.register_read_stack(temp_variable, symbol.position)
                self.generator.register_C_printf("%s", temp_variable)
            elif symbol.datatype == DataTypes.NULL:
                self.generator.register_C_printf("%s", "NULL")
