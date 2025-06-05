from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class C3DValue:
    def __init__(self, value: str, flag_temp: bool, datatype: DataTypes):
        self.value: str = value
        self.flag_temp: bool = flag_temp
        self.datatype: DataTypes = datatype
