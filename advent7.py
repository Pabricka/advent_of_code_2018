class Step:

    def __init__(self, step, prerequisite):
        self.step = step
        self.prerequisites = [prerequisite]


def correct_order():
    f = open("input7.txt", "r")
    lines = f.readlines()
    f.close()

    remaining_steps = []
    done_steps = [None]
    for line in lines:
        step = line[36]
        prerequisite = line[5]
        new = True
        for s in remaining_steps:
            if s.step == step:
                new = False
                s.prerequisites.append(prerequisite)
                break
        if new:
            remaining_steps.append(Step(step, prerequisite))
    for r in remaining_steps:
        for pre in r.prerequisites:
            new = True
            for rr in remaining_steps:
                if rr.step == pre:
                    new = False
                    break
            if new and pre is not None:
                remaining_steps.append(Step(pre, None))
    for r in remaining_steps:
        print(r.step)
        print(r.prerequisites)

    while len(remaining_steps) > 0:
        n = next_step(remaining_steps, done_steps)
        print(n)
        done_steps.append(n)
        for r in remaining_steps:
            if r.step == n:
                remaining_steps.remove(r)
                break
    order = ""
    del done_steps[0]
    for d in done_steps:
        order += d
    print(order)


def next_step(remaining_steps, done_steps):
    possible = []

    for s in remaining_steps:
        can_be_done = True
        for pre in s.prerequisites:
            check = False
            for done in done_steps:
                if pre == done:
                    check = True
                    break
            if not check:
                can_be_done = False
                break
        if can_be_done:
            possible.append(s.step)

    if len(possible) > 0:
        print(possible)
        return sorted(possible)[0]
    else:
        return -1


correct_order()
