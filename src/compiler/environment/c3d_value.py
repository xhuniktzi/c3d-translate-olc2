from compiler.environment.Generator import Generator
from compiler.expr.finals.enum_datatypes import DataTypes


class C3DValue:
    def __init__(
        self,
        value: any,
        data_type: DataTypes,
        generator: Generator,
        flag_temp: bool,
        true_label: list[str],
        false_label: list[str],
    ) -> None:
        self.value: any = value
        self.data_type: DataTypes = data_type
        self.generator: Generator = generator
        self.flag_temp: bool = flag_temp
        self.true_label: list[str] = true_label
        self.false_label: list[str] = false_label
