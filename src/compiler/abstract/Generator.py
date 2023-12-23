from compiler.expr.finals.enum_datatypes import DataTypes


class Generator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Generator")
            cls._instance = super(Generator, cls).__new__(cls)
        else:
            print("Generator already created")

        return cls._instance

    def __init__(self) -> None:
        self.temp: int = 0
        self.label: int = 0
        self.code: list[str] = []
        self.temporal_variables: list[str] = []

        self.functions: dict[str, list[str]] = {}
        self.return_functions: dict[str, DataTypes] = {}

        self.current_function: str = None  # main function

    def get_temporal_variables(self) -> str:
        return ",".join(self.temporal_variables)

    def generate_header(self) -> str:
        code_header: str = """
#include <stdio.h>
#include <math.h>

double heap[524288];
double stack[524288];

double p = 0;
double h = 0;
"""

        if len(self.temporal_variables) > 0:
            code_header += f"double {self.get_temporal_variables()};\n"

        return code_header

    def generate_define_procedure(self) -> str:
        code_define_procedure: str = ""
        for function_name, function_code in self.functions.items():
            code_define_procedure += f"void {function_name}() {{\n"
            code_define_procedure += "".join(function_code)
            code_define_procedure += "}\n"

        return code_define_procedure

    def generate_code(self) -> str:
        code_executable: str = ""
        code_executable += self.generate_header()
        code_executable += self.generate_define_procedure()
        code_executable += "int main() {\n"
        code_executable += "".join(self.code)
        code_executable += "\n"
        code_executable += "return 0;\n"
        code_executable += "}\n"

        return code_executable

    def mk_temp(self) -> str:
        temporal_variable: str = f"t{self.temp}"
        self.temp += 1

        self.temporal_variables.append(temporal_variable)
        return temporal_variable

    def mk_label(self) -> str:
        label: str = f"L{self.label}"
        self.label += 1
        return label

    def register_function(
        self, function_name: str, return_type: DataTypes = None
    ) -> None:
        self.functions[function_name] = []
        self.return_functions[function_name] = return_type

    def change_function(self, function_name: str) -> None:
        if function_name == "main":
            self.current_function = None
        else:
            self.current_function = function_name

    def register_call_function(self, function_name: str) -> None:
        code: str = f"{function_name}();\n"

        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_label(self, label: str) -> None:
        code: str = f"{label}:\n"

        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_c3d_expression(
        self, expr0: str, expr1: str, op: str, expr2: str
    ) -> None:
        code: str = f"{expr0} = {expr1} {op} {expr2};\n"

        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_if_goto(self, expr0: str, op: str, expr1: str, label: str) -> None:
        code: str = f"if ({expr0} {op} {expr1}) goto {label};\n"

        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_goto(self, label: str) -> None:
        code: str = f"goto {label};\n"

        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_C_printf(self, print_control: str, expr: str) -> None:
        code: str = f'printf("{print_control}", {expr});\n'
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_C_newline(self) -> None:
        code: str = 'printf("%c", 10);\n'
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_next_heap(self) -> None:
        code: str = "h = h + 1;\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_next_stack(self) -> None:
        code: str = "p = p + 1;\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_back_stack(self) -> None:
        code: str = "p = p - 1;\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_read_heap(self, expr0: str, expr1: str) -> None:
        code: str = f"{expr0} = heap[(int){expr1}];\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_write_heap(self, expr0: str, expr1: str) -> None:
        code: str = f"heap[(int){expr0}] = {expr1};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_read_stack(self, expr0: str, expr1: str) -> None:
        code: str = f"{expr0} = stack[(int){expr1}];\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_write_stack(self, expr0: str, expr1: str) -> None:
        code: str = f"stack[(int){expr0}] = {expr1};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def into_scope(self, offset: int) -> None:
        code: str = f"p = p + {offset};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def out_scope(self, offset: int) -> None:
        code: str = f"p = p - {offset};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def access_stack(self, expr0: str, expr1: str) -> None:
        code: str = f"{expr0} = p + {expr1};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def simple_assign(self, expr0: str, expr1: str) -> None:
        code: str = f"{expr0} = {expr1};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def simple_if(self, expr0: str, label: str) -> None:
        code: str = f"if ({expr0}) goto {label};\n"
        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)

    def register_return(self) -> None:
        code: str = "return;\n"

        if self.current_function is not None:
            self.functions[self.current_function].append(code)
        else:
            self.code.append(code)
