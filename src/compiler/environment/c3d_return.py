from compiler.environment.Generator import Generator


class C3DReturn:
    def __init__(
        self,
        generator: Generator,
        flag_return: bool,
        flag_break: bool,
        flag_continue: bool,
    ) -> None:
        self.generator: Generator = generator
        self.flag_return: bool = flag_return
        self.flag_break: bool = flag_break
        self.flag_continue: bool = flag_continue
