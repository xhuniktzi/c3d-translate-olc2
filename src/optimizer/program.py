from optimizer.assign import Assign
from optimizer.final_id import FinalId
from optimizer.goto import Goto
from optimizer.i_statement import IStatement
from optimizer.if_goto import IfGoto
from optimizer.label import Label


class Program:
    def __init__(
        self,
        temporals: list[str],
        functions: dict[str, list[IStatement]],
        main: list[IStatement],
    ) -> None:
        self.temporals: list[str] = temporals
        self.functions: dict[str, list[IStatement]] = functions
        self.main: list[IStatement] = main

    def reduce_c3d(self) -> None:
        pass

