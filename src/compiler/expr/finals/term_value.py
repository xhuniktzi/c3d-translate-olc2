from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.expr.finals.enum_datatypes import DataTypes


class TermValue(Expression):
    def __init__(self, value: any, datatype: DataTypes):
        super().__init__()
        self.value: any = value
        self.datatype: DataTypes = datatype

    def translate_to_c3d(self, env: Environment) -> C3DValue:
        if self.datatype == DataTypes.ENTERO:
            return C3DValue(f"{self.value}.0", False, self.datatype)
        elif self.datatype == DataTypes.DECIMAL:
            return C3DValue(f"{self.value}", False, self.datatype)
        elif self.datatype == DataTypes.IDVARIABLE:
            return C3DValue(f"{self.value}", False, self.datatype)
        elif self.datatype == DataTypes.CADENA:
            temp_var: str = self.generator.mk_temp()
            self.generator.simple_assign(
                temp_var, "h"
            )  # temp_var = h; save the position of the heap
            for char in self.value:
                self.generator.register_write_heap("h", f"{ord(char)}")
                self.generator.register_next_heap()

            self.generator.register_write_heap("h", "-1")  # end of string
            self.generator.register_next_heap()

            return C3DValue(temp_var, True, self.datatype)

        elif self.datatype == DataTypes.BOOLEAN:
            pass
