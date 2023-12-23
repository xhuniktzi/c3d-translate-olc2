from compiler.abstract.statement import Statement
from compiler.expr.transport.param import Param


class CallProcedure(Statement):
    def __init__(self, proc_id: str, params: list[Param]):
        self.proc_id: str = proc_id
        self.params: list[Param] = params
