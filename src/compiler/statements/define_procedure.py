from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from compiler.expr.transport.args import Args


class DefineProcedure(Statement):
    def __init__(
        self, id_proc: str, args: list[Args], statements: list[Statement]
    ) -> None:
        super().__init__()
        self.id_proc: str = id_proc
        self.args: list[Args] = args
        self.statements: list[Statement] = statements

    def translate_to_c3d(self, env: Environment):
        proc_env: Environment = Environment()

        for arg in self.args:
            proc_env.add_variable(arg.id_var, arg.datatype)

        self.generator.register_function(self.id_proc)
        self.generator.change_function(self.id_proc)

        for statement in self.statements:
            statement.translate_to_c3d(proc_env)

        self.generator.change_function("main")
