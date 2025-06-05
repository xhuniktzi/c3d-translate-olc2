import abc
from c3d.src.compiler.abstract.Generator import Generator
from c3d.src.compiler.abstract.c3d_value import C3DValue
from c3d.src.compiler.abstract.environment import Environment


from compiler.environment.environment import Environment
from compiler.expr.finals.enum_datatypes import DataTypes


class Expression(abc.ABC):
    def __init__(self):
        self.data_type: DataTypes = None
        self.true_label: list[str] = []
        self.false_label: list[str] = []

    @abc.abstractmethod
    def translate_to_c3d(self, env: Environment) -> C3DValue:
        pass
