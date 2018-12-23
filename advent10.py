class Light:

    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        self.x_pos = int(x_pos)
        self.y_pos = int(y_pos)
        self.x_vel = int(x_vel)
        self.y_vel = int(y_vel)

    def __str__(self):
        return "X: " + str(self.x_pos) + " Y: " + str(self.y_pos) + " X_velocity: " + str(self.x_vel) + " Y_velocity: " + str(self.y_vel)


f = open("input10.txt", "r")
lines = f.readlines()
f.close()

lights = []

for line in lines:
        first_comma = line.find(",")
        pos_end = line.find(">")
        second_comma = line.find(",", pos_end)
        x_pos = line[10:first_comma]
        y_pos = line[first_comma+2:pos_end]
        x_vel = line[pos_end+12:second_comma]
        y_vel = line[second_comma+2:len(line)-2]
        lights.append(Light(x_pos, y_pos, x_vel, y_vel))


def next_position(lights):
    for l in lights:
        l.x_pos += l.x_vel
        l.y_pos += l.y_vel


def previous_position(lights):
    for l in lights:
        l.x_pos -= l.x_vel
        l.y_pos -= l.y_vel


def draw_sky(lights, min_x, max_x, min_y, max_y):

    for j in range(min_y - 1, max_y + 1):
        line = ""
        for i in range(min_x - 1, max_x + 1):
            light = False
            for l in lights:
                if i == l.x_pos and j == l.y_pos:
                    line += "#"
                    light = True
                    break
            if not light:
                line += "."
        print(line)


def bounding_box(lights):
    min_x = min(lights, key=lambda l: l.x_pos).x_pos
    max_x = max(lights, key=lambda l: l.x_pos).x_pos
    min_y = min(lights, key=lambda l: l.y_pos).y_pos
    max_y = max(lights, key=lambda l: l.y_pos).y_pos
    return max_x - min_x + max_y - min_y


smallest_bounding_box = bounding_box(lights)
for i in range(15000):
    next_position(lights)
    current_bounding_box = bounding_box(lights)
    if smallest_bounding_box >= current_bounding_box:
        smallest_bounding_box = current_bounding_box
    else:
        print("smallest bounding box is " + str(current_bounding_box))
        print("after " + str(i) + " seconds")
        break


previous_position(lights)
min_x = min(lights, key=lambda l: l.x_pos).x_pos
max_x = max(lights, key=lambda l: l.x_pos).x_pos
min_y = min(lights, key=lambda l: l.y_pos).y_pos
max_y = max(lights, key=lambda l: l.y_pos).y_pos

draw_sky(lights, min_x, max_x, min_y, max_y)
