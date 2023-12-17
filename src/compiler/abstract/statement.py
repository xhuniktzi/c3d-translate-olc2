import abc
from compiler.abstract.Generator import Generator


class Statement(abc.ABC):
    def __init__(self):
        self.generator = Generator()

    @abc.abstractmethod
    def translate_to_c3d(self):
        pass
