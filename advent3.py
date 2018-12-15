def squares_that_intersect():
    f = open("input3.txt", "r")
    lines = f.readlines()
    f.close()

    fabric = [[0 for i in range(1000)] for j in range(1000)]

    for line in lines:
        first = line.find("@")
        second = line.find(",")
        third = line.find(":")
        fourth = line.find("x")

        left = int(line[first+2:second])
        top = int(line[second+1:third])
        width = int(line[third+2:fourth])
        height = int(line[fourth+1:])
        for i in range(width):
            for j in range(height):
                fabric[left+i][top+j] += 1

    counter = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[0])):
            if fabric[i][j] > 1:
                counter += 1
    print(str(counter) + " inches of cloth overlap")
    return fabric


fab = squares_that_intersect()


def claim_that_doesnt_overlap(fabric):

    f = open("input3.txt", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        first = line.find("@")
        second = line.find(",")
        third = line.find(":")
        fourth = line.find("x")

        claim = int(line[1:first])
        no_intersect = True

        left = int(line[first+2:second])
        top = int(line[second+1:third])
        width = int(line[third+2:fourth])
        height = int(line[fourth+1:])
        for i in range(width):
            for j in range(height):
                if fabric[left+i][top+j] > 1:
                    no_intersect = False
        if no_intersect:
            print("claim with id " + str(claim) + " does not overlap!")


claim_that_doesnt_overlap(fab)
