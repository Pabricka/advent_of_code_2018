import datetime


def remaining_polymer(string):

    units = []
    for c in string:
        if c.isprintable():
            units.append(c)

    iterate = True
    while iterate:
        iterate = False

        for i in range(len(units)-1):
            if i < len(units)-1:
                if units[i].isupper():
                    if units[i].lower() == units[i+1]:
                        del units[i]
                        del units[i]

                        iterate = True
                else:
                    if units[i].upper() == units[i+1]:
                        del units[i]
                        del units[i]
                        iterate = True
    return len(units)


def shortest_polymer(string):
    shortest = len(string)
    types = set()
    for c in string:
        if c.isprintable():
            types.add(c.lower())

    for t in types:
        tmp = filter(lambda char: char not in [t, t.upper()], string)
        length = remaining_polymer(tmp)
        print("with removal of " + t + " and " + t.upper() + " polymer is " + str(length) + " units long")
        if length < shortest:
            shortest = length
    print("shortest possible polymer is " + str(shortest) + " units long")


f = open("input5.txt", "r")
s = f.readline()
f.close()

print(datetime.datetime.now())
print(remaining_polymer(s))
shortest_polymer(s)
print(datetime.datetime.now())
