from compiler.abstract.environment import Environment
from compiler.abstract.statement import Statement
from compiler.expr.transport.args import Args


class DefineProcedure(Statement):
    def __init__(
        self, id_proc: str, args: list[Args], statements: list[Statement]
    ) -> None:
        self.id_proc: str = id_proc
        self.args: list[Args] = args
        self.statements: list[Statement] = statements

    def translate_to_c3d(self, env: Environment):
        return super().translate_to_c3d(env)
