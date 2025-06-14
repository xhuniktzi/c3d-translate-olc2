from __future__ import annotations

from c3d.src.compiler.abstract.c3d_symbol import C3DSymbol
from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


class Environment:
    def __init__(self) -> None:
        # self.parent: Environment = parent
        self.variables: dict[str, C3DSymbol] = {}
        self.size: int = 0

        # if parent is not None:
        #     self.size = parent.size

    def add_variable(self, identifier: str, datatype: DataTypes) -> None:
        if self.variables.get(identifier) is not None:
            print(f"Variable {identifier} already exists in this scope")
            return

        variable: C3DSymbol = C3DSymbol(identifier, datatype, self.size)
        self.size += 1
        self.variables[identifier] = variable

        return variable

    def get_variable(self, identifier: str) -> C3DSymbol:
        # local_env: Environment = self
        # while local_env is not None:
        # if local_env.variables.get(identifier) is not None:
        #     return local_env.variables[identifier]
        #     # local_env = local_env.parent

        if self.variables.get(identifier) is not None:
            return self.variables[identifier]

        print(f"Variable {identifier} does not exist in this scope")
        return None
