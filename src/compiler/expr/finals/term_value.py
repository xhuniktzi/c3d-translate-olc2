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

        # if self.datatype != DataTypes.CADENA:
        #     return C3DValue(self.value, False, self.datatype)
        # elif self.datatype == DataTypes.CADENA:
        #     temp_var: str = self.generator.mk_temp()
        #     self.generator.register_c3d(temp_var, f'"{self.value}"')
        #     return C3DValue(temp_var, True, self.datatype)
