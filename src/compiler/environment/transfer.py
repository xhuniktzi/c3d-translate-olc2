from compiler.environment.transfer_enum import TransferTypes


class Transfer:
    def __init__(self, transer_type: TransferTypes, label_jump: str, value_flag: bool):
        self.transfer_type: TransferTypes = transer_type
        self.label_jump: str = label_jump
        self.value_flag: bool = value_flag
