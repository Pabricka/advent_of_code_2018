class Guard:

    def __init__(self, guard_id="default_id"):
        self.guard_id = guard_id
        self.time_slept = 0
        self.minutes = [0 for i in range(60)]


def sleepiest_guard():

    f = open("input4.txt", "r")
    lines = f.readlines()
    f.close()
    lines.sort()

    guards = []

    # lets make a list of all guards
    for l in lines:
        new = True
        if l.find("#") > 0:
            gid = l.split(" ")[3]
            for g in guards:
                if g.guard_id == gid:
                    new = False
        else:
            new = False
        if new:
            guards.append(Guard(l.split(" ")[3]))

    # lets check how much they sleep
    current_guard = None
    fell_asleep = None
    for l in lines:
        if l.find("#") > 0:
            current_guard = l.split(" ")[3]
            fell_asleep = None
        minutes = int(l[l.find(":")+1:l.find(":")+3])
        if l.split(" ")[3] == "asleep\n":
            fell_asleep = int(minutes)
        if l.split(" ")[3] == "up\n":
            for g in guards:
                if g.guard_id == current_guard:
                    g.time_slept += minutes - fell_asleep
                    while fell_asleep<minutes:
                        g.minutes[fell_asleep] += 1
                        fell_asleep += 1

    # who slept most?

    sleepyhead = guards[0]
    for g in guards:
        if g.time_slept > sleepyhead.time_slept:
            sleepyhead = g
        print("Guard number " + g.guard_id + " slept for " + str(g.time_slept) + " minutes")
    print("Guard number " + sleepyhead.guard_id + " was the most sleepiest by "
          + str(sleepyhead.time_slept) + " minutes!")

    finest_minute = 0
    index = 0

    for i, m in enumerate(sleepyhead.minutes):
        if m > finest_minute:
            finest_minute = m
            index = i
    print("They are probably sleep at 00:" + str(index))

    finest_minute = 0
    times = 0
    guard = guards[0]
    for m in range(60):
        for g in guards:
            if g.minutes[m] > times:
                print(g.guard_id + " sleeps at minute " + str(m) + " " + str(g.minutes[m]) + " times")
                times = g.minutes[m]
                finest_minute = m
                guard = g
    print(guard.guard_id + " is most frequently asleep at " + str(finest_minute))


sleepiest_guard()
