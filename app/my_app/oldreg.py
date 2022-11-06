try:
    import sys
    from bitfields import Bits
    from enum import Enum

except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class Registers:
    r0 = 0
    r1 = 1
    r2 = 2
    r3 = 3
    r4 = 4
    r5 = 5
    r6 = 6
    r7 = 7
    r8 = 8
    r9 = 9
    r10 = 10
    r11 = 11
    r12 = 12
    SP = 13
    LR = 14
    PCPSR = 15

    def __init__(self, names=None, values=None, **kwargs):
        self.names = names or ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7',
                               'r8', 'r9', 'r10', 'r11', 'r12',
                               'SP', 'LR', 'PC  CPSR']
        self.values = []
        if values:
            if (len(values) > 16):
                for i in range(16):
                    self.values.append(Bits(values[i]))
            else:
                self.values = [reg for reg in values]
                self.values += [Bits(0) * 17 - len(self.values)]
        else:
            self.values = [Bits(0) * 16]

    def __len__(self):
        return len(self.names)

    def __call__(self, reg):
        if 0 <= reg <= 15:
            return self.values[reg]

    def print(self, style="b"):
        values = printRegValues(style)


    def printRegValues(self, style="b"):
        if (style == 'd'):
            return [int(reg) for reg in self.values]
        elif (style == 'x'):
            return [
                ("0x" + "".join([byte[:2]
                 for byte in str(bytes(reg).split('\\x')[1:])]))
                for reg in self.values
                ]
        else:
            return ["0b" + "".join(list(reg)) for reg in self.values]

