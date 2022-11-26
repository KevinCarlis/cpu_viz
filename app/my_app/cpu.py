try:
    import sys
    from my_app import registers
    from enum import Enum
    from bitfields import Bits
except ImportError as err:
    print(f"Unable to load module: registers.\n{err}")
    sys.exit(2)

class REGNAMES (Enum):
    R0: 0 
	R1: 1
	R2: 2
	R3: 3
	R4: 4
	R5: 5
	R6: 6
    R7: 7
	R8: 8
    R9: 9
    R10: 10
	R11: 11
	R12: 12
    SP: 13
	LR: 14
	PC_CPSR: 15

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
        self.cpsr = CPSR[cpsr]
        self.s = (s == "Up")
        self.i = (rn == "Immediate")
		self.ins = INS[ins]
		self.rd = rd
		self.rm = rm
		self.rn = rn
		self.immbits = immbits
		self.immshift = immshift

	def encode():
		bits = str(self.cpsr)
		bits += '1' if self.s else '0'
		bits += '1' if self.i else '0'
		bits += str(self.ins)
		for i in range(len(Registers.names)):
			if (Registers.names[i] == self.rd):
				rd = bin(i)[2:].zfill(4)
			if (Registers.names[i] == self.rm):
				rm = bin(i)[2:].zfill(4)
			if (Registers.names[i] == self.rn):
				rn = bin(i)[2:].zfill(4)
		bits += rd + rm
		if not self.i:
			bits += rn + "00"
		else
			bits += bin(self.immbits)[2:].zfill(4) + bin(self.immshift)[2:].zfill(4)
		return bits


	def decode(ins):
		bits = list(Bits(ins))
		bits = ([0] * (24 - len(bits))) + bits
		self.cpsr = CPSR(bits[0]*8 + bits[1]*4 + bits[2]*2 + bits[3])
		self.s = bool(bits[4])
		self.i = bool(bits[5])
		self.ins = CPSR(bits[6]*8 + bits[7]*4 + bits[8]*2 + bits[9])
		self.rd = Registers.names[(bits[10]*8 + bits[11]*4 + bits[12]*2 + bits[13])]
		self.rm = Registers.names[(bits[14]*8 + bits[15]*4 + bits[16]*2 + bits[17])]
		self.rn = Registers.names[(bits[18]*8 + bits[19]*4 + bits[20]*2 + bits[21])]
		if (self.i):
			self.rn = 'Immediate'
			self.immbits = Bits.from_binary('0b' + "".join([str(i) for i in bits[18:22]])
			self.immshift = Bits(bits[22]*2 + bits[23])


class CPU:
    def __init__(self):
		self.registers = cpu_part.Registers()
		self.instruction = cpu_part.Instruction()

	def encode(self, **kwargs):
		self.instruction.encode(**kwargs)
		self.registers = registers

	def execute(self):
		if (self.cpsr()):
			self.alu()

	def cpsr(self):
		flag = self.instruction.cpsr
		if (flag == 'AL'): return True
		if (flag == 'NV'): return False
		register = self.registers[15]
		if (flag == 'NE')

	def alu(self):
		ins = self.instruction.ins


if __name__ == "__main__":
    pass
