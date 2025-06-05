from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class C3DSymbol:
    def __init__(self, identifier: str, datatype: DataTypes, position: int):
        self.identifier: str = identifier
        self.datatype: DataTypes = datatype
        self.position: int = position
