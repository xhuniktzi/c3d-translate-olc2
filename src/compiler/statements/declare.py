from compiler.abstract.c3d_value import C3DValue
from compiler.abstract.statement import Statement


class Declare(Statement):
    def __init__(self, identifier: str, datatype: str):
        super().__init__()
        self.identifier: str = identifier
        self.datatype: str = datatype

    def translate_to_c3d(self):
        pass
