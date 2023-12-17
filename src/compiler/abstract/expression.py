import abc
from compiler.abstract.Generator import Generator


class Expression(abc.ABC):
    def __init__(self):
        self.generator = Generator()
        self.true_label: str = ""
        self.false_label: str = ""

    @abc.abstractmethod
    def translate_to_c3d(self):
        pass
