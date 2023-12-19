from compiler.expr.finals.enum_datatypes import DataTypes


class Symbol:
    def __init__(
        self, sym_id: str, datatype: DataTypes, heap_index: int, init_flag: bool
    ):
        self.sym_id: str = sym_id
        self.datatype: DataTypes = datatype
        self.heap_index: int = heap_index
        self.init_flag: bool = init_flag
