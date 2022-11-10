try:
    import sys
    from my_app import registers
    from enum import Enum
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class CPSR(Enum):
    AL = 0
    EQ = 1
    NE = 2
    GE = 3
    GT = 4
    LE = 5
    LT = 6
    CS = 7
    CC = 8
    MI = 9
    PL = 10
    VS = 11
    VC = 12
    HI = 13
    LS = 14
    NV = 15

    def __str__(self):
        return bin(self.value)[2:].zfill(4)


class Instruction:
    def __init__(
            self, ins='Mov', cpsr='AL', upcpsr=None,
            rd='R0', rm='R0', rn='R0',
            immbits=None, immshift=None):
        for status in CPSR:
            if status.name == cpsr:
                self.cpsr = status
                break
        self.s = (s == "Up")
        self.i = True


class CPU:
    def __init__(self, regnames=None):
        self.registers = regnames or [
            'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6',
            'R7', 'R8', 'R9', 'R10', 'R11', 'R12',
            'SP', 'LR', 'PC', 'CPSR'
        ]


if __name__ == "__main__":
    pass
