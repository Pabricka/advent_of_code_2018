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





def number_of_opcodes(lines):
    register_before = []
    instructions = []
    possible_opcode_numbers = [set() for i in range(16)]
    for line in lines:
        if line.startswith("Before"):
            register_before = [int(s) for s in line.strip()[9:len(line.strip("\n"))-1].split(",")]
        elif line.startswith("After"):
            register_after = [int(s) for s in line[9:len(line.strip("\n"))-1].split(",")]
            operations = [addr(register_before, instructions), addi(register_before, instructions),
                          mulr(register_before, instructions), muli(register_before, instructions),
                          banr(register_before, instructions), bani(register_before, instructions),
                          borr(register_before, instructions), bori(register_before, instructions),
                          setr(register_before, instructions), seti(register_before, instructions),
                          gtir(register_before, instructions), gtri(register_before, instructions),
                          gtrr(register_before, instructions), eqir(register_before, instructions),
                          eqri(register_before, instructions), eqrr(register_before, instructions)]
            for i, o in enumerate(operations):
                if o == register_after:
                    possible_opcode_numbers[i].add(instructions[0])

        else:
            instructions = [int(s) for s in line.split()]
    opcode_numbers = [None for i in range(16)]

    finished = False
    while not finished:
        finished = True
        for i, p in enumerate(possible_opcode_numbers):
            if len(p) == 1:
                number = p.pop()
                opcode_numbers[number] = i
                for po in possible_opcode_numbers:
                    po.discard(number)
                    finished = False
    return opcode_numbers


def execute_test(lines, opcodes):
    register = [0, 0, 0, 0]
    for line in lines:
        instructions = [int(s) for s in line.split()]
        op = instructions[0]
        operations = [addr(register, instructions), addi(register, instructions),
                      mulr(register, instructions), muli(register, instructions),
                      banr(register, instructions), bani(register, instructions),
                      borr(register, instructions), bori(register, instructions),
                      setr(register, instructions), seti(register, instructions),
                      gtir(register, instructions), gtri(register, instructions),
                      gtrr(register, instructions), eqir(register, instructions),
                      eqri(register, instructions), eqrr(register, instructions)]
        register = operations[opcodes[op]]
    return register[0]


f = open("input16.txt", "r")
lines = f.readlines()
f = open("input16_2.txt", "r")
lines2 = f.readlines()
f.close()
print("Answer to part 1: " + str(three_or_more_opcodes(lines)))
op = number_of_opcodes(lines)
print("Answer to part 2: " + str(execute_test(lines2, op)))
