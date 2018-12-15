def frequency_after_all_changes():
    f = open("input1.txt", "r")
    lines = f.readlines()
    f.close()
    answer = 0
    for i, line in enumerate(lines):
        answer += int(line)
    print("frequency after all achanges is: " + str(answer))


def first_frequency_that_appears_twice():
    numbers = []
    visited = set()
    visited.add(0)
    current = 0
    f = open("input1.txt", "r")
    lines = f.readlines()
    f.close()

    found = False

    print("starting frequency is: 0")
    while not found:
        for i, line in enumerate(lines):
            print("change of: " + line)

            numbers.append(line)
            current += int(line)
            print("current frequency is: " + str(current))
            if current in visited:
                print("that is also the answer!")
                return
            visited.add(current)
            if found:
                break


frequency_after_all_changes()
first_frequency_that_appears_twice()
