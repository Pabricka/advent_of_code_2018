def addr(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] + register[b]
    return register


def addi(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] + b
    return register


def mulr(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] * register[b]
    return register


def muli(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] * b
    return register


def banr(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] & register[b]
    return register


def bani(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] & b
    return register


def borr(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] | register[b]
    return register


def bori(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = register[a] | b
    return register


def setr(register, instructions):
    register = register.copy()
    a = instructions[1]
    c = instructions[3]

    register[c] = register[a]
    return register


def seti(register, instructions):
    register = register.copy()
    a = instructions[1]
    c = instructions[3]

    register[c] = a
    return register


def gtir(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = int(a > register[b])
    return register


def gtri(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = int(register[a] > b)
    return register


def gtrr(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = int(register[a] > register[b])
    return register


def eqir(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = int(a == register[b])
    return register


def eqri(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = int(register[a] == b)
    return register


def eqrr(register, instructions):
    register = register.copy()
    a = instructions[1]
    b = instructions[2]
    c = instructions[3]

    register[c] = int(register[a] == register[b])
    return register


def three_or_more_opcodes(lines):
    register_before = []
    instructions = []
    three_or_more = 0
    for line in lines:
        if line.startswith("Before"):
            register_before = [int(s) for s in line.strip()[9:len(line.strip("\n"))-1].split(",")]
        elif line.startswith("After"):
            register_after = [int(s) for s in line[9:len(line.strip("\n"))-1].split(",")]
            counter = 0
            operations = [addr(register_before, instructions), addi(register_before, instructions),
                          mulr(register_before, instructions), muli(register_before, instructions),
                          banr(register_before, instructions), bani(register_before, instructions),
                          borr(register_before, instructions), bori(register_before, instructions),
                          setr(register_before, instructions), seti(register_before, instructions),
                          gtir(register_before, instructions), gtri(register_before, instructions),
                          gtrr(register_before, instructions), eqir(register_before, instructions),
                          eqri(register_before, instructions), eqrr(register_before, instructions)]
            for o in operations:
                if o == register_after:
                    counter += 1
            if counter >= 3:
                three_or_more += 1

        else:
            instructions = [int(s) for s in line.split()]

    return three_or_more


f = open("input16.txt", "r")
lines = f.readlines()
f.close()
print(three_or_more_opcodes(lines))
