from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class OrExpr(Expression):
    def __init__(self, left: Expression, right: Expression):
        super().__init__()
        self.left: Expression = left
        self.right: Expression = right

    def translate_to_c3d(self, env: Environment) -> C3DValue:
        true_label: str = self.generator.mk_label()
        false_label: str = self.generator.mk_label()

        left_eval: C3DValue = self.left.translate_to_c3d(env)
        right_eval: C3DValue = self.right.translate_to_c3d(env)

        left_eval = self.handle_variable(left_eval, env)
        right_eval = self.handle_variable(right_eval, env)

        self.generator.register_if_goto(left_eval.value, "==", "1", true_label)
        self.generator.register_if_goto(right_eval.value, "==", "1", true_label)
        self.generator.register_goto(false_label)

        temp_var: str = self.generator.mk_temp()
        self.generator.register_label(true_label)
        self.generator.simple_assign(temp_var, "1")

        exit_label: str = self.generator.mk_label()
        self.generator.register_goto(exit_label)

        self.generator.register_label(false_label)
        self.generator.simple_assign(temp_var, "0")
        self.generator.register_label(exit_label)

        return C3DValue(temp_var, False, DataTypes.BOOLEAN, true_label, false_label)

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
