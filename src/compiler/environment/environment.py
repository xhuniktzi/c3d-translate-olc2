from __future__ import annotations
from compiler.environment.symbol import Symbol
from compiler.environment.transfer import Transfer

from compiler.expr.finals.enum_datatypes import DataTypes


class Environment:
    def __init__(self, parent: Environment, return_type: DataTypes = None):
        self.parent: Environment = parent
        self.symbols: dict[str, Symbol] = {}
        self.size = 0
        self.child_envs: list[Environment] = []

        self.list_transfer_controllers: list[Transfer] = []
        self.return_type: DataTypes = return_type

        self.temp_vars: list[str] = []
        self.function_env_flag: bool = False

    def add_symbol(self, var_id: str, datatype: DataTypes, init_flag: bool) -> Symbol:
        new_symbol: Symbol = self.symbols.get(var_id)
        if new_symbol is None:
            new_symbol = Symbol(var_id, datatype, self.size, init_flag)
            self.symbols[var_id] = new_symbol
            self.size += 1

            return new_symbol
