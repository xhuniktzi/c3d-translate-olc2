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

    def get_temporal_variables(self) -> str:
        return "".join(self.temporal_variables)

    def generate_header(self) -> str:
        code_header: str = """
            #include <stdio.h>
            #include <math.h>

            double heap[78000];
            double stack[78000];

            double p = 0;
            double h = 0;
            """

        if len(self.temporal_variables) > 0:
            code_header += f"double {self.get_temporal_variables()};\n"

        return code_header

    def generate_code(self) -> str:
        code_executable: str = ""
        code_executable += self.generate_header()

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

    def register_call_function(self, function_name: str) -> None:
        self.code.append(f"{function_name}();\n")

    def register_label(self, label: str) -> None:
        self.code.append(f"{label}:\n")

    def register_c3d_expression(
        self, expr0: str, expr1: str, op: str, expr2: str
    ) -> None:
        self.code.append(f"{expr0} = {expr1} {op} {expr2};\n")

    def register_if_goto(self, expr0: str, op: str, expr1: str, label: str) -> None:
        self.code.append(f"if ({expr0} {op} {expr1}) goto {label};\n")

    def register_C_printf(self, print_control: str, expr: str) -> None:
        self.code.append(f'printf("{print_control}", {expr});\n')

    def register_next_heap(self) -> None:
        self.code.append("h = h + 1;\n")

    def register_next_stack(self) -> None:
        self.code.append("p = p + 1;\n")

    def register_back_stack(self) -> None:
        self.code.append("p = p - 1;\n")

    def register_read_heap(self, expr0: str, expr1: str) -> None:
        self.code.append(f"{expr0} = heap[{expr1}];\n")

    def register_write_heap(self, expr0: str, expr1: str) -> None:
        self.code.append(f"heap[{expr0}] = {expr1};\n")

    def register_read_stack(self, expr0: str, expr1: str) -> None:
        self.code.append(f"{expr0} = stack[{expr1}];\n")

    def register_write_stack(self, expr0: str, expr1: str) -> None:
        self.code.append(f"stack[{expr0}] = {expr1};\n")
