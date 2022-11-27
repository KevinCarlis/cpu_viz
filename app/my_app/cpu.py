try:
    import sys
    from py_app import parts
    from enum import Enum
    from bitfields import Bits
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)


class CPU:
    def __init__(self, reg_size=8):
        self.reg_size = reg_size
        self.registers = parts.Registers(reg_size)
        self.instructions = parts.Instructions()

    def encode(self, registers=None, insreg=0, **kwargs):
        if (registers):
            self.registers = registers
        self.instructions[insreg].encode(**kwargs)

    def execute(self, insreg=0, **kwargs):
        self.fetch(ins=ins)
        self.decode(**kwargs)
        self.execute()
        self.writeback()

    def fetch(self, insreg):
        self.instruction = self.instructions[insreg]

    def decode(self, **kwargs):
        self.instruction.decode(**kwargs)

    def execute(self):
        if (self.cpsr()):
            self.alu()

    def writeback(self):
        if (self.result):
            self.registers[self.instruction.rd.value].value = self.result
        if (self.instruction.s):
            self.registers[15].value = (self.registers[15].value[:4] * 16) + Bits(self.registers.N*8 + self.registers.Z*4 + self.registers.C*2 + self.registers.v)

    def cpsr(self):
        flag = self.instruction.cpsr.name
        if (flag == 'AL'): return True
        elif (flag == 'EQ' and self.registers.Z == 1): return True
        elif (flag == 'NE' and self.registers.Z == 0): return True
        elif (flag == 'CS' and self.registers.C == 1): return True
        elif (flag == 'CC' and self.registers.C == 0): return True
        elif (flag == 'MI' and self.registers.N == 1): return True
        elif (flag == 'PL' and self.registers.N == 0): return True
        elif (flag == 'VS' and self.registers.V == 1): return True
        elif (flag == 'VC' and self.registers.V == 0): return True
        elif (flag == 'HI' and self.registers.Z == 0 and self.registers.C == 1): return True
        elif (flag == 'LS' and (self.registers.Z == 1 or self.registers.C == 0)): return True
        elif (flag == 'GE' and self.registers.N == self.registers.V): return True
        elif (flag == 'LT' and self.registers.N != self.registers.V): return True
        elif (flag == 'GT' and self.registers.Z == 0 and self.registers.N == self.registers.V): return True
        elif (flag == 'LE' and self.registers.Z == 1 and self.registers.N != self.registers.V): return True
        return False

    def alu(self):
        ins = self.instruction.ins.name
        s = self.instruction.s
        i = self.instruction.i
        rm = c.registers[self.instruction.rm.value].value
        if (i):
            rn = Bits(self.instruction.immbits * 2 * self.instruction.immshift)
        else:
            rn = c.registers[self.instruction.rn.value].value
        if (flag == 'MOV'):
            if (s):
                self.registers.Z = 1 if rn else 0
                self.registers.N = 0 if (rn < (2**(reg_size-1))) else 1 
                self.registers.C = 0
                self.registers.V = 0
            self.result = rn 
        elif (flag == 'CMP'): return
        elif (flag == 'ADD'): return
        elif (flag == 'ADC'): return
        elif (flag == 'SUB'): return
        elif (flag == 'SBC'): return
        elif (flag == 'MUL'): return
        elif (flag == 'DIV'): return
        elif (flag == 'AND'): return
        elif (flag == 'BIC'): return
        elif (flag == 'ORR'): return
        elif (flag == 'EOR'): return
        elif (flag == 'LSL'): return
        elif (flag == 'LSR'): return
        elif (flag == 'ASR'): return
        elif (flag == 'ROR'): return


if __name__ == "__main__":
    c = CPU()
    print(c.instructions())
