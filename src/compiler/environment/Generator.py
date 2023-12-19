from __future__ import annotations
import compiler.environment.conf as conf
from compiler.environment.environment import Environment


class Generator:
    def __init__(self, env: Environment):
        self.env: Environment = env
        self.code: list[str] = []
        self.temp_vars: list[str] = []

    def generate_temporaries(self) -> str:
        return ",".join([f" {i}" for i in range(conf.counter_temporary)])

    def generate_code(self) -> str:
        return "\n".join(self.code)

    def get_final_code(self) -> str:
        self.generate_main()
        self.code = conf.f_code + self.code
        self.generate_temporaries_header()
        self.generate_headers()

        return "\n".join(self.code)

    def combine(self, gen: Generator) -> Generator:
        self.code += gen.code[:]
        self.temp_vars
        return self

    def generate_main(self):
        self.code = [
            "int main() {",
            f"    {self.generate_code()}\n",
            "    return 0;",
            "}",
        ]

    def generate_temporaries_header(self):
        if conf.counter_temporary > 0:
            self.code = [f"double {self.generate_temporaries()};\n", f"{self.code}"]

    def generate_headers(self):
        a = self.code[::]
        self.code = [
            "#include <stdio.h>",
            "#include <stdlib.h>",
            "#include <math.h>",
            "double HEAP[100000];",
            "double STACK[100000];",
            "double P = 0;",
            "double H = 0;",
        ]

        self.code += a

    def mk_temp(self, persistance_flag: bool) -> str:
        temp_var: str = f"t{conf.counter_temporary}"
        self.temp_vars.append(conf.counter_temporary)
        conf.counter_temporary += 1
        if persistance_flag:
            pass

        return temp_var

    def register_func_call(self, func_name: str):
        self.code.append(f"    {func_name}();")

    def register_labels(self, labels: list[str]):
        if len(labels) > 0:
            for lbl in labels:
                if lbl != "":
                    self.code.append(f"{lbl}:")

    def register_c3d_expression(self, target: str, left: str, op: str, right: str):
        self.code.append(f"    {target} = {left} {op} {right};")

    def register_cast(self, target: str, datatype: str, value: str):
        self.code.append(f"    {target} = ({datatype}) {value};")

    def regster_if_goto(self, left: str, op: str, right: str, label: str):
        self.code.append(f"    if({left} {op} {right}) goto {label};")

    def register_goto(self, label: str):
        self.code.append(f"    goto {label};")

    def register_C_printf(self, print_type: str, value: str):
        self.code.append(f'    printf("{print_type}", {value});')

    def register_C_print_string(self, value: str):
        for char in value:
            self.code.append(f'    printf("%c", {ord(char)});')

    def register_C_newline(self):
        self.code.append('printf("%c", 10);')

    def register_next_heap(self):
        self.code.append("    H = H + 1;")

    def register_next_stack(self, index: str):
        self.code.append(f"    P = P + {index};")

    def register_back_stack(self, index: str):
        self.code.append(f"    P = P - {index};")

    def register_read_heap(self, target: str, index: str):
        self.code.append(f"    {target} = HEAP[(int){index}];")

    def register_write_heap(self, index: str, value: str):
        self.code.append(f"    HEAP[(int){index}] = {value};")

    def register_read_stack(self, target: str, index: str):
        self.code.append(f"    {target} = STACK[(int){index}];")

    def register_write_stack(self, index: str, value: str):
        self.code.append(f"    STACK[(int){index}] = {value};")

    def register_call(self, func_name: str):
        self.code.append(f"    {func_name}();")
