import abc
from compiler.abstract.Generator import Generator
from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.environment import Environment


class Expression(abc.ABC):
    def __init__(self):
        self.generator = Generator()
        # self.true_label: str = ""
        # self.false_label: str = ""

    @abc.abstractmethod
    def translate_to_c3d(self, env: Environment) -> C3DValue:
        pass
