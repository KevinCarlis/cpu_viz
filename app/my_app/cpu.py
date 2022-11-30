try:
    import sys
    from . import parts
    from bitfields import Bits
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class CPU:
    def __init__(self, reg_size=8):
        self.reg_size = reg_size
        self.registers = parts.Registers(reg_size)
        self.instructions = parts.Instructions()

    def encode(self, inscheck=0, **kwargs):
        self.instructions[int(inscheck)][1].decode(**kwargs)

    def run(self, inscheck=0, **kwargs):
        self.fetch(int(inscheck))
        self.decode()
        if (self.cpsr()):
            self.execute()
            self.writeback()
        self.registers.format()

    def fetch(self, insreg):
        self.instruction = self.instructions[insreg][1]

    def decode(self):
        self.flag = self.instruction.cpsr.name
        self.ins = self.instruction.ins.name
        self.s = self.instruction.s
        self.i = self.instruction.i
        self.rd = self.instruction.rd.value
        self.rm = self.registers[self.instruction.rm.value].value
        if (self.i):
            self.rn = Bits(self.instruction.immbits)
            for _ in range(self.instruction.immshift):
                self.rn *= 2
        else:
            self.rn = self.registers[self.instruction.rn.value].value
        cpsr = "".join(
            [str(b) for b in list(self.registers.cpsr.value)]
        ).zfill(8)
        self.N = int(cpsr[4])
        self.Z = int(cpsr[5])
        self.C = int(cpsr[6])
        self.V = int(cpsr[7])

    def execute(self):
        self.alu()

    def writeback(self):
        cpsr = self.cpsr_result()
        if (self.ins != 'CMP'):
            self.registers[self.rd].value = self.result
        if (self.s or self.ins == 'CMP'):
            self.registers.cpsr.value = self.registers[15].value >> 4
            self.registers.cpsr.value = self.registers[15].value << 4
            self.registers.cpsr.value += Bits.from_binary(cpsr)
        self.registers = self.registers

    def cpsr_result(self):
        if (self.result.bit_length() > self.reg_size):
            v = '1'
            self.result = self.result[-(self.reg_size):]
        else:
            v = '0'
        cpsr = ''
        cpsr += '0' if (self.result < (2**(self.reg_size-1))) else '1'
        cpsr += '0' if self.result else '1'
        cpsr += '0'
        cpsr += v
        return cpsr

    def cpsr(self):
        if (self.flag == 'AL'): return True
        elif (self.flag == 'EQ' and self.Z == 1): return True
        elif (self.flag == 'NE' and self.Z == 0): return True
        elif (self.flag == 'CS' and self.C == 1): return True
        elif (self.flag == 'CC' and self.C == 0): return True
        elif (self.flag == 'MI' and self.N == 1): return True
        elif (self.flag == 'PL' and self.N == 0): return True
        elif (self.flag == 'VS' and self.V == 1): return True
        elif (self.flag == 'VC' and self.V == 0): return True
        elif (self.flag == 'HI' and self.Z == 0 and self.C == 1): return True
        elif (self.flag == 'LS' and (self.Z == 1 or self.C == 0)): return True
        elif (self.flag == 'GE' and self.N == self.V): return True
        elif (self.flag == 'LT' and self.N != self.V): return True
        elif (self.flag == 'GT' and self.Z == 0 and self.N == self.V): return True
        elif (self.flag == 'LE' and self.Z == 1 and self.N != self.V): return True
        return False

    def alu(self):
        if (self.ins == 'MOV'):
            self.result = self.rn
        elif (self.ins == 'CMP'):
            self.result = self.rm - self.rn
        elif (self.ins == 'ADD'):
            self.result = self.rn + self.rm
        elif (self.ins == 'ADC'):
            self.result = self.rn + self.rm + int(self.registers.c)
        elif (self.ins == 'SUB'):
            self.result = self.rm - self.rn
        elif (self.ins == 'SBC'):
            self.result = self.rm - self.rn - int(self.registers.c)
        elif (self.ins == 'MUL'):
            self.result = self.rn * self.rm
        elif (self.ins == 'DIV'):
            self.result = self.rm / self.rm
        elif (self.ins == 'AND'):
            self.result = self.rm & self.rn
        elif (self.ins == 'BIC'):
            self.result = self.rm & (~self.rn)
        elif (self.ins == 'ORR'):
            self.result = self.rm | self.rn
        elif (self.ins == 'EOR'):
            self.result = self.rm ^ self.rn
        elif (self.ins == 'LSL'):
            self.result = self.rm << self.rn
        elif (self.ins == 'LSR'):
            self.result = self.rm >> self.rn
        elif (self.ins == 'ASR'):
            self.result = self.rm >> self.rn
            if self.rm.bit_length == 8:
                self.result += Bits.from_binary(0b10000000)
        elif (self.ins == 'ROR'):
            self.result = self.rm
            for _ in self.rn:
                if (self.result % 2 == 1):
                    self.result += Bits.from_binary(0b100000000)
                self.result = self.result >> 1
