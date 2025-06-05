from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.abstract.statement import Statement
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class Assign(Statement):
    def __init__(self, identifier: str, value: Expression):
        super().__init__()
        self.identifier: str = identifier
        self.value: Expression = value

    def translate_to_c3d(self, env: Environment):
        variable_eval: C3DValue = self.value.translate_to_c3d(env)
        symbol: C3DSymbol = env.get_variable(self.identifier)

        if symbol is None:
            return

        temp_var: str = self.generator.mk_temp()
        self.generator.access_stack(temp_var, symbol.position)
        self.generator.register_write_stack(temp_var, variable_eval.value)
