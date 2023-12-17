from compiler.abstract.c3d_symbol import C3DSymbol
from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from compiler.expr.finals.enum_datatypes import DataTypes


class Declare(Statement):
    def __init__(self, identifier: str, datatype: DataTypes):
        super().__init__()
        self.identifier: str = identifier
        self.datatype: DataTypes = datatype

    def translate_to_c3d(self, env: Environment):
        pass
        # symbol: C3DSymbol = env.add_variable(self.identifier, self.datatype)

        # self.generator.register_write_stack(symbol.position, "0")
