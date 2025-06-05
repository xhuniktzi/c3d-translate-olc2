from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.abstract.statement import Statement
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class ReturnStatement(Statement):
    def __init__(self, expr: Expression):
        super().__init__()
        self.expr: Expression = expr

    def translate_to_c3d(self, env: Environment):
        if self.expr is None:
            self.generator.register_return()
            return

        temp_var: str = self.generator.mk_temp()

        variable_eval: C3DValue = self.expr.translate_to_c3d(env)
        variable_eval = self.handle_variable(variable_eval, env)

        self.generator.simple_assign(temp_var, variable_eval.value)

        stack_var: str = self.generator.mk_temp()
        self.generator.access_stack(stack_var, 0)
        self.generator.register_write_stack(stack_var, temp_var)
        self.generator.register_return()

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
