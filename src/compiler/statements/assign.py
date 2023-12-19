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
        pass
