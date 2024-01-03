from optimizer.assign import Assign
from optimizer.final_id import FinalId
from optimizer.i_statement import IStatement


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
        self.rule_1_main()
        self.rule_1_functions()
        

    # Removal of Redundant Instructions
    # Rule 1: a = b; b = a; -> a = b;
    # On main
    def rule_1_main(self):
        assigns: dict[str, str] = {}
        code: list[IStatement] = []

        for statement in self.main:
            if isinstance(statement, Assign):
                left = statement.target
                right = statement.expr.var_id if isinstance(statement.expr, FinalId) else None

                if right is not None and left in assigns and right == assigns[left]:
                    print(f"On main, applying rule 1: {left} = {right}; {right} = {left}; -> {left} = {right};")
                    continue

                assigns[left] = right
            code.append(statement)
        self.main = code

    # Removal of Redundant Instructions
    # Rule 1: a = b; b = a; -> a = b;
    # On functions
    def rule_1_functions(self):
        for function in self.functions:
            assigns: dict[str, str] = {}
            code: list[IStatement] = []

            for statement in self.functions[function]:
                if isinstance(statement, Assign):
                    left = statement.target
                    right = statement.expr.var_id if isinstance(statement.expr, FinalId) else None

                    if right is not None and left in assigns and right == assigns[left]:
                        print(f"On function {function}, applying rule 1: {left} = {right}; {right} = {left}; -> {left} = {right};")
                        continue

                    assigns[left] = right
                code.append(statement)
            self.functions[function] = code
        
