class Step:

    def __init__(self, step, prerequisite):
        self.step = step
        self.prerequisites = [prerequisite]
        self.time = 60 + ord(step.lower()) - 96


def correct_order():
    f = open("input7.txt", "r")
    lines = f.readlines()
    f.close()

    remaining_steps = []
    done_steps = [None]

    in_doing = []

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
        print("step " + r.step)
        print("prerequisites are: ")
        print(r.prerequisites)
        print("this step will take " + str(r.time) + " seconds")

    time_lapsed = 0
    while len(remaining_steps) > 0 or len(in_doing) > 0:
        n = next_step(remaining_steps, done_steps)
        if len(in_doing) < 5 and n is not -1:
            print("lets do " + n.step)
            in_doing.append(n)
            for r in remaining_steps:
                if r.step == n.step:
                    remaining_steps.remove(r)
                    break
        else:
            if len(in_doing) == 0:
                break
            print("time is moving forward....")
            shortest = in_doing[0]
            for d in in_doing:
                if shortest.time > d.time:
                    shortest = d
            for d in in_doing:
                if d.step != shortest.step:
                    d.time -= shortest.time
            time_lapsed += shortest.time
            print("done: " + shortest.step + " it took " + str(shortest.time) + " seconds")
            done_steps.append(shortest.step)
            in_doing.remove(shortest)

    order = ""
    print(time_lapsed)
    del done_steps[0]
    for d in done_steps:
        order += d
    print("steps were done in order: " + order)


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
            possible.append(s)

    if len(possible) > 0:
        return sorted(possible, key=lambda x: x.step)[0]
    else:
        return -1


correct_order()
