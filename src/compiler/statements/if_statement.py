from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.expression import Expression
from compiler.abstract.statement import Statement


class IfStatement(Statement):
    def __init__(
        self,
        expr: Expression,
        statements: list[Statement],
        else_statements: list[Statement] = None,
    ):
        super().__init__()
        self.expr: Expression = expr
        self.statements: list[Statement] = statements
        self.else_statements: list[Statement] = else_statements

    def translate_to_c3d(self, env):
        expr_value: C3DValue = self.expr.translate_to_c3d(env)

        if self.else_statements is None:
            true_label = self.generator.mk_label()
            exit_label = self.generator.mk_label()

            self.generator.register_if_goto(expr_value.value, "==", "1", true_label)
            self.generator.register_goto(exit_label)

            self.generator.register_label(true_label)
            for statement in self.statements:
                statement.translate_to_c3d(env)

            self.generator.register_label(exit_label)

        else:
            true_label = self.generator.mk_label()
            false_label = self.generator.mk_label()
            exit_label = self.generator.mk_label()

            self.generator.register_if_goto(expr_value.value, "==", "1", true_label)
            self.generator.register_goto(false_label)

            self.generator.register_label(true_label)
            for statement in self.statements:
                statement.translate_to_c3d(env)
            self.generator.register_goto(exit_label)

            self.generator.register_label(false_label)
            for statement in self.else_statements:
                statement.translate_to_c3d(env)

            self.generator.register_label(exit_label)
