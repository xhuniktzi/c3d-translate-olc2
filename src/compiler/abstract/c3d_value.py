from compiler.expr.finals.enum_datatypes import DataTypes


class C3DValue:
    def __init__(
        self,
        value: str,
        flag_temp: bool,
        datatype: DataTypes,
        false_label: str = None,
        true_label: str = None,
    ):
        self.value: str = value
        self.flag_temp: bool = flag_temp
        self.datatype: DataTypes = datatype

        self.false_label: str = false_label
        self.true_label: str = true_label
