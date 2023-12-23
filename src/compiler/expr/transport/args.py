from compiler.expr.finals.enum_datatypes import DataTypes


class Args:
    def __init__(self, id_var: str, datatype: DataTypes) -> None:
        self.id_var: str = id_var
        self.datatype: DataTypes = datatype
