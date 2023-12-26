from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment
from compiler.abstract.expression import Expression
from compiler.abstract.statement import Statement


class WhileStatement(Statement):
    def __init__(self, condition: Expression, statements: list[Statement]):
        super().__init__()
        self.condition: Expression = condition
        self.statements: list[Statement] = statements

    def translate_to_c3d(self, env: Environment):
        loop_label: str = self.generator.mk_label()

        self.generator.register_label(loop_label)
        condition_value: C3DValue = self.condition.translate_to_c3d(env)
        exit_label: str = self.generator.mk_label()

        self.generator.register_if_goto(condition_value.value, "==", "0", exit_label)
        for statement in self.statements:
            statement.translate_to_c3d(env)
        self.generator.register_goto(loop_label)
        self.generator.register_label(exit_label)
