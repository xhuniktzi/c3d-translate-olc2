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
            self.generator.register_C_newline()
        elif variable_eval.datatype == DataTypes.CADENA:
            temp_variable: str = self.generator.mk_temp()
            self.generator.register_c3d_expression(
                temp_variable, variable_eval.value, "", ""
            )
            init_label: str = self.generator.mk_label()
            continue_label: str = self.generator.mk_label()

            self.generator.register_label(init_label)
            self.generator.register_if_goto(
                f"heap[(int){temp_variable}]", "==", "-1", continue_label
            )
            self.generator.register_C_printf("%c", f"(int)heap[(int){temp_variable}]")
            self.generator.register_c3d_expression(
                temp_variable, temp_variable, "+", "1"
            )
            self.generator.register_goto(init_label)
            self.generator.register_label(continue_label)
            self.generator.register_C_newline()

        elif variable_eval.datatype == DataTypes.IDVARIABLE:
            symbol = env.get_variable(variable_eval.value)
            if symbol is None:
                return

            temp_variable: str = self.generator.mk_temp()
            if symbol.datatype == DataTypes.ENTERO:
                self.generator.register_read_stack(temp_variable, symbol.position)
                self.generator.register_C_printf("%d", f"(int){temp_variable}")
                self.generator.register_C_newline()
            elif symbol.datatype == DataTypes.DECIMAL:
                self.generator.register_read_stack(temp_variable, symbol.position)
                self.generator.register_C_printf("%f", f"(double){temp_variable}")
                self.generator.register_C_newline()
            # elif symbol.datatype == DataTypes.CADENA:
            #     self.generator.register_read_stack(temp_variable, symbol.position)
            #     self.generator.register_C_printf("%s", temp_variable)
            # elif symbol.datatype == DataTypes.NULL:
            #     self.generator.register_C_printf("%s", "NULL")
            #     self.generator.register_C_newline()
