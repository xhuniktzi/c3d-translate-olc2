from compiler.abstract.c3d_symbol import C3DSymbol
from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.abstract.statement import Statement
from compiler.expr.finals.enum_datatypes import DataTypes


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

        # if symbol.datatype != variable_eval.datatype:
        #     print(f"Cannot assign {variable_eval.datatype} to {symbol.datatype}")
        #     return

        self.generator.register_write_stack(symbol.position, variable_eval.value)
