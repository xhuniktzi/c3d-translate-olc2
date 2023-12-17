from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.expression import Expression
from compiler.expr.finals.enum_datatypes import DataTypes


class TermValue(Expression):
    def __init__(self, value: any, datatype: DataTypes):
        super().__init__()
        self.value: any = value
        self.datatype: DataTypes = datatype

    def translate_to_c3d(self) -> C3DValue:
        pass
