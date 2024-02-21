from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.statement import Statement
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class Declare(Statement):
    def __init__(self, identifier: str, datatype: DataTypes):
        super().__init__()
        self.identifier: str = identifier
        self.datatype: DataTypes = datatype

    def translate_to_c3d(self, env: Environment):
        env.add_variable(self.identifier, self.datatype)
