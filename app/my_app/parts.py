try:
    import sys
    from bitfields import Bits
    from enum import Enum
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class REG(Enum):
    R0  = 0 
    R1  = 1
    R2  = 2
    R3  = 3
    R4  = 4
    R5  = 5
    R6  = 6
    R7  = 7
    R8  = 8
    R9  = 9
    R10 = 10
    R11 = 11
    R12 = 12
    SP  = 13
    LR  = 14
    PC_CPSR = 15

    def __str__(self):
        return bin(self.value)[2:].zfill(4)


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


class INS(Enum):
    MOV = 0
    CMP = 1
    ADD = 2
    ADC = 3
    SUB = 4
    SBC = 5
    MUL = 6
    DIV = 7
    AND = 8
    BIC = 9
    ORR = 10
    EOR = 11
    LSL = 12
    LSR = 13
    ASR = 14
    ROR = 15

    def __str__(self):
        return bin(self.value)[2:].zfill(4)



class Register:
    def __init__(self, name, size=8, value=Bits(0)):
        self.name = name
        self.size = size
        self.value = value

    def format(self):
        return (
            self.name,
            "0b" + self.bin(),
            "0x" + self.hex(),
            self.decimal()
        )

    def decimal(self):
        if int(self.value) < (2**(self.size-1)):
            return int(self.value)
        return int(self.value) - (2**self.size)

    def hex(self):
        ret = "".join([
            byte[:2] for byte in str(bytes(self.value)).split('\\x')[1:]
            ]).zfill(self.size//4)
        if (self.name == 'PC_CPSR'):
            ret = ret[:-1] + '|' + ret[-1:]
        return ret

    def bin(self):
        ret = str(self.value)[2:].zfill(self.size)
        if (self.name == 'PC_CPSR'):
            ret = ret[:-4] + '|' + ret[-4:]
        return ret


class Registers:
    def __init__(self, reg_size=8):
        self._registers = []
        for name in REG._member_names_:
            self._registers.append(Register(name, size=reg_size))
        self._strings = self.format()

    def __len__(self):
        return len(self.registers)

    def __call__(self):
        return self._strings
    
    def __getitem__(self, key):
        return self.registers[key]

    def get_names(self):
        return REG._member_names_

    def format(self):
        return [reg.format() for reg in self.registers]

    @property
    def registers(self):
        return self._registers

    @registers.setter
    def registers(self, value):
        self._registers = value
        self.N = str(self._registers[REG["PC_CPSR"]])[4]
        self.Z = str(self._registers[REG["PC_CPSR"]])[5]
        self.C = str(self._registers[REG["PC_CPSR"]])[6]
        self.V = str(self._registers[REG["PC_CPSR"]])[7]
        self.PC = str(self._registers[REG["PC_CPSR"]])[:4]

class Instruction:
    def __init__(
            self, ins='MOV', cpsr='AL', upcpsr=None,
            rd='R0', rm='R0', rn='R0',
            immbits=None, immshift=None):
        self.cpsr = CPSR[cpsr]
        self.s = (upcpsr == "Up")
        if (rn == "Immediate"):
            self.i = True
            self.rn = "Immediate"
        else:
            self.i = False
            self.rn = REG[rn]
        self.ins = INS[ins]
        self.rd = REG[rd]
        self.rm = REG[rm]
        self.immbits = immbits
        self.immshift = immshift

    def encode(self):
        bits = str(self.cpsr)
        bits += '1' if self.s else '0'
        bits += '1' if self.i else '0'
        bits += str(self.ins)
        bits += str(self.rd) 
        bits += str(self.rm)
        if not self.i:
            bits += str(self.rn) + "00"
        else:
            bits += bin(self.immbits)[2:].zfill(4) + bin(self.immshift)[2:].zfill(4)
        return bits

    def decode(self, ins):
        bits = list(Bits(ins))
        bits = ([0] * (24 - len(bits))) + bits
        self.cpsr = CPSR(bits[0]*8 + bits[1]*4 + bits[2]*2 + bits[3])
        self.s = bool(bits[4])
        self.i = bool(bits[5])
        self.ins = CPSR(bits[6]*8 + bits[7]*4 + bits[8]*2 + bits[9])
        self.rd = REG(bits[10]*8 + bits[11]*4 + bits[12]*2 + bits[13])
        self.rm = REG(bits[14]*8 + bits[15]*4 + bits[16]*2 + bits[17])
        if not self.i:
            self.rn = REG(bits[18]*8 + bits[19]*4 + bits[20]*2 + bits[21])
            self.immbits = None
            self.immshift = None
        else:
            self.rn = 'Immediate'
            self.immbits = Bits.from_binary('0b' + "".join([str(i) for i in bits[18:22]]))
            self.immshift = Bits(bits[22]*2 + bits[23])


class Instructions:
    def __init__(self, rows=16, size=3):
        self.instructions = []
        for i in range(rows):
            self.instructions.append([i,Instruction()])

    def __call__(self):
        ret = []
        for row in self.instructions:
            bits = row[1].encode()
            ret.append([
                row[0],
                "0b" + bits[:8],
                bits[8:16],
                bits[16:]
            ])
        return ret

    def __getitem__(self, key):
        return self.instructions[key]


if __name__ == "__main__":
    i = Registers()
    r = REG.R0
    print(r)
