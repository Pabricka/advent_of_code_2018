from advent16 import addr, addi, setr, seti, mulr, muli, gtir, gtri, gtrr, eqri, eqir, eqrr

f = open("input19.txt", "r")
lines = f.readlines()
f.close()
ip = int(lines[0].strip("\n")[3:])
lines.pop(0)
register = [0, 0, 0, 0, 0, 0]
while register[ip] < len(lines):
    instruction = [lines[register[ip]].split()[0]]
    instruction.extend([int(x) for x in lines[register[ip]].strip("\n").split() if x.isdigit()])
    if instruction[0] == "addr":
        register = addr(register, instruction)
    elif instruction[0] == "addi":
        register = addi(register, instruction)
    elif instruction[0] == "setr":
        register = setr(register, instruction)
    elif instruction[0] == "seti":
        register = seti(register, instruction)
    elif instruction[0] == "mulr":
        register = mulr(register, instruction)
    elif instruction[0] == "muli":
        register = muli(register, instruction)
    elif instruction[0] == "qtir":
        register = gtir(register, instruction)
    elif instruction[0] == "gtri":
        register = gtri(register, instruction)
    elif instruction[0] == "gtrr":
        register = gtrr(register, instruction)
    elif instruction[0] == "eqri":
        register = eqri(register, instruction)
    elif instruction[0] == "eqir":
        register = eqir(register, instruction)
    elif instruction[0] == "eqrr":
        register = eqrr(register, instruction)
    register[ip] += 1
print(register)
