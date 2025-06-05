from c3d.src.compiler.abstract.environment import Environment
from c3d.src.compiler.abstract.expression import Expression
from c3d.src.compiler.abstract.statement import Statement
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes
from c3d.src.compiler.expr.transport.args import Args


class DefineFunction(Statement):
    def __init__(
        self,
        id_func: str,
        args: list[Args],
        statements: list[Statement],
        return_type: DataTypes,
    ):
        super().__init__()
        self.id_func: str = id_func
        self.args: list[Args] = args
        self.statements: list[Statement] = statements
        self.return_type: DataTypes = return_type

    def translate_to_c3d(self, env: Environment):
        func_env = Environment()

        func_env.add_variable("__ret__", self.return_type)

        for arg in self.args:
            func_env.add_variable(arg.id_var, arg.datatype)

        self.generator.register_function(self.id_func, self.return_type)
        self.generator.change_function(self.id_func)

        for statement in self.statements:
            statement.translate_to_c3d(func_env)

        self.generator.change_function("main")
