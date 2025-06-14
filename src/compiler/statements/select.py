from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.abstract.statement import Statement
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class Select(Statement):
    def __init__(self, expr: Expression):
        super().__init__()
        self.expr: Expression = expr

    def translate_to_c3d(self, env: Environment):
        variable_eval: C3DValue = self.expr.translate_to_c3d(env)

        if variable_eval.datatype == DataTypes.ENTERO:
            self.generator.register_C_printf("%d", f"(int){variable_eval.value}")
            self.generator.register_C_newline()

        elif variable_eval.datatype == DataTypes.DECIMAL:
            self.generator.register_C_printf("%f", f"(double){variable_eval.value}")
            self.generator.register_C_newline()
        elif variable_eval.datatype == DataTypes.CADENA:
            temp_variable: str = self.generator.mk_temp()
            self.generator.simple_assign(temp_variable, variable_eval.value)
            init_label: str = self.generator.mk_label()
            continue_label: str = self.generator.mk_label()

            self.generator.register_label(init_label)

            heap_variable: str = self.generator.mk_temp()
            self.generator.register_read_heap(heap_variable, temp_variable)

            self.generator.register_if_goto(heap_variable, "==", "-1", continue_label)

            self.generator.register_C_printf("%c", f"(int){heap_variable}")
            self.generator.register_c3d_expression(
                temp_variable, temp_variable, "+", "1"
            )
            self.generator.register_goto(init_label)
            self.generator.register_label(continue_label)
            self.generator.register_C_newline()

        elif variable_eval.datatype == DataTypes.BOOLEAN:
            true_label: str = self.generator.mk_label()
            false_label: str = self.generator.mk_label()
            exit_label: str = self.generator.mk_label()

            self.generator.register_if_goto(variable_eval.value, "==", "1", true_label)
            self.generator.register_goto(false_label)

            self.generator.register_label(true_label)
            self.generator.register_C_printf("%c", "84")
            self.generator.register_goto(exit_label)

            self.generator.register_label(false_label)
            self.generator.register_C_printf("%c", "70")

            self.generator.register_label(exit_label)
            self.generator.register_C_newline()

        elif variable_eval.datatype == DataTypes.IDVARIABLE:
            symbol = env.get_variable(variable_eval.value)
            if symbol is None:
                return

            if symbol.datatype == DataTypes.ENTERO:
                temp_variable: str = self.generator.mk_temp()
                stack_variable: str = self.generator.mk_temp()

                self.generator.access_stack(stack_variable, symbol.position)
                self.generator.register_read_stack(temp_variable, stack_variable)

                self.generator.register_C_printf("%d", f"(int){temp_variable}")
                self.generator.register_C_newline()
            elif symbol.datatype == DataTypes.DECIMAL:
                temp_variable: str = self.generator.mk_temp()
                stack_variable: str = self.generator.mk_temp()

                self.generator.access_stack(stack_variable, symbol.position)
                self.generator.register_read_stack(temp_variable, stack_variable)

                self.generator.register_C_printf("%f", f"(double){temp_variable}")
                self.generator.register_C_newline()
            elif symbol.datatype == DataTypes.CADENA:
                temp_variable: str = self.generator.mk_temp()
                stack_variable: str = self.generator.mk_temp()

                self.generator.access_stack(stack_variable, symbol.position)
                self.generator.register_read_stack(temp_variable, stack_variable)

                init_label: str = self.generator.mk_label()
                continue_label: str = self.generator.mk_label()

                self.generator.register_label(init_label)

                heap_variable: str = self.generator.mk_temp()
                self.generator.register_read_heap(heap_variable, temp_variable)

                self.generator.register_if_goto(
                    heap_variable, "==", "-1", continue_label
                )

                self.generator.register_C_printf("%c", f"(int){heap_variable}")
                self.generator.register_c3d_expression(
                    temp_variable, temp_variable, "+", "1"
                )
                self.generator.register_goto(init_label)
                self.generator.register_label(continue_label)
                self.generator.register_C_newline()

            elif symbol.datatype == DataTypes.BOOLEAN:
                temp_variable: str = self.generator.mk_temp()
                stack_variable: str = self.generator.mk_temp()

                self.generator.access_stack(stack_variable, symbol.position)
                self.generator.register_read_stack(temp_variable, stack_variable)

                true_label: str = self.generator.mk_label()
                false_label: str = self.generator.mk_label()
                exit_label: str = self.generator.mk_label()

                self.generator.register_if_goto(temp_variable, "==", "1", true_label)
                self.generator.register_goto(false_label)

                self.generator.register_label(true_label)
                self.generator.register_C_printf("%c", "84")
                self.generator.register_goto(exit_label)

                self.generator.register_label(false_label)
                self.generator.register_C_printf("%c", "70")

                self.generator.register_label(exit_label)
                self.generator.register_C_newline()
