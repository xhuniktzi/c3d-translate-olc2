from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.statement import Statement
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes
from c3d.src.compiler.expr.transport.param import Param


class CallProcedure(Statement):
    def __init__(self, proc_id: str, params: list[Param]):
        super().__init__()
        self.proc_id: str = proc_id
        self.params: list[Param] = params

    def translate_to_c3d(self, env: Environment):
        last_stack: str = self.generator.mk_temp()
        self.generator.simple_assign(last_stack, env.size)  # tn = P + size

        # create temporal variables for each param
        list_temp_params: list[str] = []
        for param in self.params:
            temp_var: str = self.generator.mk_temp()
            list_temp_params.append(temp_var)

            param_eval: C3DValue = param.expr.translate_to_c3d(env)
            param_eval = self.handle_variable(param_eval, env)

            self.generator.simple_assign(temp_var, param_eval.value)

        # change scope
        self.generator.into_scope(env.size)
        for i in range(len(self.params)):
            temp_var: str = self.generator.mk_temp()
            self.generator.access_stack(temp_var, i)
            self.generator.register_write_stack(temp_var, list_temp_params[i])

        # call function
        self.generator.register_call_function(self.proc_id)

        # return to scope
        self.generator.out_scope(env.size)

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
