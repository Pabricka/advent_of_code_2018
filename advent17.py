import sys

sys.setrecursionlimit(3000)
f = open("input17.txt", "r")
lines = f.readlines()
f.close()

clays = []
waters = []
spring = [500, 0]
for line in lines:
    if line.startswith("x"):
        x = int(line[2:line.find(",")])
        y_start = int(line[line.find("y")+2: line.find(".")])
        y_end = int(line[line.find(".")+2:])
        for y in range(y_start, y_end+1):
            clays.append([x, y])
    else:
        y = int(line[2:line.find(",")])
        x_start = int(line[line.find("x")+2: line.find(".")])
        x_end = int(line[line.find(".")+2:])
        for x in range(x_start, x_end+1):
            clays.append([x, y])

min_x = min(clays, key=lambda x: x[0])[0]
max_x = max(clays, key=lambda x: x[0])[0]
min_y = min(clays, key=lambda x : x[1])[1]
max_y = max(clays, key=lambda x : x[1])[1]
ground = [["." for i in range(max_x+2)] for i in range(max_y+2)]
ground[spring[1]][spring[0]] = "+"
for c in clays:
    ground[c[1]][c[0]] = "#"


def draw_ground(ground):
    for y in range(min_y, max_y):
        s = ""
        for x in range(min_x-2, max_x+2):
            s += ground[y][x]
        print(s)


ground[spring[1]+1][spring[0]] = "|"


def flow_water(ground, x, y, d):
    #draw_ground(ground)
    if ground[y][x] == ".":
        ground[y][x] = "|"
    if y >= max_y:
        return
    if ground[y][x] == "#":
        return x
    if ground[y+1][x] == ".":
        flow_water(ground, x, y+1, 0)
    if ground[y+1][x] == "#" or ground[y+1][x] == "~":
        if d:
            return flow_water(ground, x+d, y, d)
        left = flow_water(ground, x-1, y, -1)
        right = flow_water(ground, x+1, y, 1)
        if ground[y][left] == "#" and ground[y][right] == "#":
            for i in range(left+1, right):
                ground[y][i] = "~"
    else:
        return x


flow_water(ground, spring[0], spring[1]+1, 0)
counter = 0
draw_ground(ground)
for y in range(min_y, max_y+1):
    for x in range(min_x-2, max_x+2):
        if ground[y][x] == "|" or ground[y][x] == "~":
            counter += 1
print("water can reach: " + str(counter) + " tiles")
counter = 0
for y in range(min_y, max_y+1):
    for x in range(min_x-2, max_x+2):
        if ground[y][x] == "~":
            counter += 1
print("amount of water stored: " + str(counter))
