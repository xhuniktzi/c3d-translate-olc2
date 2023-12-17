from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.abstract.statement import Statement
from compiler.expr.finals.enum_datatypes import DataTypes


class Select(Statement):
    def __init__(self, expr: Expression):
        super().__init__()
        self.expr: Expression = expr

    def translate_to_c3d(self, env: Environment):
        variable_eval: C3DValue = self.expr.translate_to_c3d()

        if variable_eval.datatype == DataTypes.ENTERO:
            self.generator.register_C_printf("%d", variable_eval.value)
        elif variable_eval.datatype == DataTypes.IDVARIABLE:
            symbol = env.get_variable(variable_eval.value)
            if symbol is None:
                return
            if symbol.datatype == DataTypes.ENTERO:
                self.generator.register_C_printf("%d", symbol.value)
            elif symbol.datatype == DataTypes.DECIMAL:
                self.generator.register_C_printf("%f", symbol.value)
            elif symbol.datatype == DataTypes.CADENA:
                self.generator.register_C_printf("%s", symbol.value)
            elif symbol.datatype == DataTypes.NULL:
                self.generator.register_C_printf("%s", "NULL")
