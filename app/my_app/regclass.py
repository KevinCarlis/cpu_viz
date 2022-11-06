try:
    import sys
    from bitfields import Bits
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class Register:
    def __init__(self, name, value=Bits(255)):
        self.name = name
        self.value = value

    def format(self):
        return (self.name, self.bin(), self.hex(), self.decimal())

    def decimal(self):
        return int(self.value)

    def hex(self):
        lead = '0' * ((8 - self.value.bit_length())//2)
        ret = "0x" + lead + "".join([
            byte[:2] for byte in str(bytes(self.value)).split('\\x')[1:]
            ])
        if (self.name == 'PC  CPSR'):
            ret = ret[:-1] + '|' + ret[-1:]
        return ret

    def bin(self):
        lead = '0' * (7 - self.value.bit_length())
        ret = "0b" + lead + str(self.value)[2:]
        if (self.name == 'PC  CPSR'):
            ret = ret[:-4] + '|' + ret[-4:]
        return ret


class Registers:
    names = [
            'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6',
            'R7', 'R8', 'R9', 'R10', 'R11', 'R12',
            'SP', 'LR', 'PC  CPSR'
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


class Instructions:
    def __init__(self, rows=10, size=3):
        self.instructions = []
        for i in range(rows):
            instruction = [i*size]
            for j in range(size):
                instruction.append(Register(i*size+j))
            self.instructions.append(instruction)

    def __call__(self):
        ret = []
        for row in self.instructions:
            strings = [row[0]]
            for i in row[1:]:
                strings.append(i.bin())
            ret.append(strings)
        return ret

if __name__ == "__main__":
    i = Instructions()
    print(i())
