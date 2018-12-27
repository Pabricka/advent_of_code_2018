class Rule:

    def __init__(self, sequence, result):
        self.sequence = sequence
        self.result = result

    def __str__(self):
        return self.sequence + " => " + self.result


def generation(state, rules):
    new_state = state[:1]
    for i in range(1, len(state)-1):
        match = False
        for r in rules:
            if state[i-1:i+4] == r.sequence:
                new_state += r.result
                match = True
                break
        if not match:
            new_state += "."
    return "...." + new_state + "...."


f = open("input12.txt", "r")
lines = f.readlines()
f.close()

initial_state = "...." + lines[0].strip("\n")[15:] + "...."
rules = []
for i in range(2, len(lines)):
    if lines[i][9] == "#":
        rules.append(Rule(lines[i][:5], lines[i][9]))

new = initial_state
zero = 4
stabilize, last_sum, difference, start, counter = 0, 0, 0, 0, 0
j = 0
while stabilize < 10:
    counter = 0
    new = generation(new, rules)
    zero += 3
    # left
    for i in range(zero):
        if new[i] == "#":
            counter -= zero - i

    # right
    for i in range(zero, len(new)):
        if new[i] == "#":
            counter += i - zero
    if counter-last_sum == difference:
        stabilize += 1
        if start == 0:
            start = counter
    else:
        stabilize = 0
        start = 0
    j += 1
    if j == 20:
        print("answer to part 1: " + str(counter))
    difference = counter-last_sum
    last_sum = counter
print("difference after " + str(j-10) + " stabilizes at: " + str(difference))
print("after 50000000000 generations sum is... : " + str(+ (50000000000-j)*difference + counter))


