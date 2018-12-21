class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


def largest_area():
    f = open("input6.txt", "r")
    lines = f.readlines()
    f.close()

    points = []

    for line in lines:
        comma = line.find(",")
        x = line[:comma]
        y = line.rstrip("\n")[comma+2:]
        points.append(Point(x, y))

    biggest_y = 0
    smallest_y = points[0].y
    biggest_x = 0
    smallest_x = points[0].x
    for p in points:
        if p.x > biggest_x:
            biggest_x = p.x
        if p.x < smallest_x:
            smallest_x = p.x
        if p.y > biggest_y:
            biggest_y = p.y
        if p.y < smallest_y:
            smallest_y = p.y

    grid = [[[] for i in range(smallest_x-1, biggest_x+2)] for j in range(smallest_y+1, biggest_y+2)]
    areas = [0 for i in range(len(points))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            distances = []
            for point in points:
                distances.append(abs(i-point.x) + abs(j-point.y))
            grid[i][j] = distances

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            distance = grid[i][j][0]
            index = 0
            near = True
            for d in range(len(points)):
                if grid[i][j][d] < distance:
                    index = d
                    distance = grid[i][j][d]
            for d in range(len(points)):
                if grid[i][j][d] == distance and d != index:
                    near = False
            if i == len(grid) or i == 0 or j == len(grid[0]) or j == 0:
                areas[index] = -1

            if areas[index] >= 0:
                areas[index] += near

    biggest_area = 0
    for a in areas:
        if a > biggest_area:
            biggest_area = a

    print("biggest area is: " + str(biggest_area))

    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = sum(grid[i][j])
            if s < 10000:
                c += 1
    print("area with maximum combined distance from all points is: " + str(c))


largest_area()
