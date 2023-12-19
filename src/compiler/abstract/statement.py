import abc

from compiler.environment.c3d_return import C3DReturn
from compiler.environment.environment import Environment


class Statement(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def translate_to_c3d(self, env: Environment) -> C3DReturn:
        pass
