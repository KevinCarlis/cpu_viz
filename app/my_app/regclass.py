try:
    import sys
    from bitfields import Bits
    from enum import Enum
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class Register:
    def __init__(self, name, value=Bits(0)):
        self.name = name
        self.value = value

    def format(self):
        return (
            self.name,
            "0b" + self.bin(),
            "0x" + self.hex(),
            self.decimal()
        )

    def decimal(self):
        if int(self.value) < 128:
            return int(self.value)
        return int(self.value) - 256

    def hex(self):
        ret = "".join([
            byte[:2] for byte in str(bytes(self.value)).split('\\x')[1:]
            ]).zfill(2)
        if (self.name == 'PC CPSR'):
            ret = ret[:-1] + '|' + ret[-1:]
        return ret

    def bin(self):
        ret = str(self.value)[2:].zfill(8)
        if (self.name == 'PC CPSR'):
            ret = ret[:-4] + '|' + ret[-4:]
        return ret


class Registers:
    names = [
            'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6',
            'R7', 'R8', 'R9', 'R10', 'R11', 'R12',
            'SP', 'LR', 'PC CPSR'
            ]

    def __init__(self):
        self.registers = [Register(name) for name in self.get_names()]
        self._strings = self.format()

    def __len__(self):
        return len(self.registers)

    def __call__(self):
        return self._strings

    def get_names(self):
        return Registers.names

    def format(self):
        return [reg.format() for reg in self.registers]


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
    def __init__(self, cpsr, s, i, opcode, rn, rd, rm):
        for status in CPSR:
            if status.name == cpsr:
                self.cpsr = status
                break
        self.s = (s == "Up")
        self.i = True


class Instructions:
    def __init__(self, rows=16, size=3):
        self.instructions = []
        for i in range(rows):
            instruction = [i]
            for j in range(size):
                instruction.append(Register(i*size+j))
            self.instructions.append(instruction)

    def __call__(self):
        ret = []
        for row in self.instructions:
            ret.append([
                row[0],
                "0b" + row[1].bin(),
                row[2].bin(),
                row[3].bin()
            ])
        return ret


if __name__ == "__main__":
    i = Instructions()
    print(i())
