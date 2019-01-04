import copy
f = open("input18.txt", "r")
lines = f.readlines()
f.close()
area = [["." for i in range(len(lines[0])-1)] for i in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[0].strip("\n"))):
        area[i][j] = lines[i][j]


def draw_area(area):
    print()
    for i in range(len(area)):
        s = ""
        for j in range(len(area[0])):
            s += area[i][j]
        print(s)
    print()

def change_landscape(area):
    new_area = copy.deepcopy(area)
    for i in range(len(area)):
        for j in range(len(area[0])):
            adjacent = ""
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= i+k < len(area) and 0 <= j+l < len(area[0]):
                            adjacent += area[i+k][j+l]
                adjacent += "\n"
            if area[i][j] == ".":
                if adjacent.count("|") >= 3:
                    new_area[i][j] = "|"
            elif area[i][j] == "|":
                if adjacent.count("#") >= 3:
                    new_area[i][j] = "#"
            elif area[i][j] == "#":
                if adjacent.count("#") >= 2 and adjacent.count("|") >= 1:
                    continue
                else:
                    new_area[i][j] = "."
    #draw_area(new_area)
    return new_area


for i in range(10):
    area = change_landscape(area)

lumberyards = 0
trees = 0
for a in area:
    lumberyards += a.count("#")
    trees += a.count("|")
print(lumberyards * trees)