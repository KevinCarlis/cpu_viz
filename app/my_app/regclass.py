try:
    import sys
    from bitfields import Bits
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class Register:
    def __init__(self, name, value=Bits(15)):
        self.name = name
        self.value = value

    def pair(self, style='b'):
        if (style == 'd'):
            return (self.name, int(self.value))
        elif (style == 'x'):
            lead = '0' * ((8 - self.value.bit_length())//2)
            ret = "0x" + lead + "".join([
                byte[:2] for byte in str(bytes(self.value)).split('\\x')[1:]
            ])
            if (self.name == 'PC  CPSR'):
                ret = ret[:-2] + '|' + ret[-2:]
            return (self.name, ret)
        else:
            lead = '0' * (7 - self.value.bit_length())
            ret = "0b" + lead + str(self.value)[2:]
            if (self.name == 'PC  CPSR'):
                ret = ret[:-4] + '|' + ret[-4:]
            return (self.name, ret)


class Registers:
    def __init__(self, style='b', **kwargs):
        self.names = [
            'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6',
            'R7', 'R8', 'R9', 'R10', 'R11', 'R12',
            'SP', 'LR', 'PC  CPSR'
        ]
        self.registers = [Register(name) for name in self.names]
        self.format(style)

    def __len__(self):
        return len(self.registers)

    def format(self, style="b"):
        self.printable = [reg.pair(style) for reg in self.registers]

    def get_names(self):
        return Registers.names
