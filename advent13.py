class Cart:

    def __init__(self, facing, x_pos, y_pos):

        # accidentally mixed x and y...
        # x_pos is really Y coordinate of the cart and vice versa with y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.facing = facing
        self.next_turn = "left"


def move_carts(track, carts):
    carts.sort(key=lambda x: (x.x_pos, x.y_pos))

    colliding_carts = []
    collision = False
    for cart in carts:
        # diagonal
        if track[cart.x_pos][cart.y_pos] == "|":
            if cart.facing == "v":
                cart.x_pos += 1
            if cart.facing == "^":
                cart.x_pos -= 1
        # horizontal
        elif track[cart.x_pos][cart.y_pos] == "-":
            if cart.facing == ">":
                cart.y_pos += 1
            if cart.facing == "<":
                cart.y_pos -= 1
        # intersection
        elif track[cart.x_pos][cart.y_pos] == "+":
            turn_cart(cart)
        # corners
        elif track[cart.x_pos][cart.y_pos] == "/":
            if cart.facing == "<":
                cart.x_pos += 1
                cart.facing = "v"
            elif cart.facing == "v":
                cart.y_pos -= 1
                cart.facing = "<"
            elif cart.facing == ">":
                cart.x_pos -= 1
                cart.facing = "^"
            elif cart.facing == "^":
                cart.y_pos += 1
                cart.facing = ">"
        elif track[cart.x_pos][cart.y_pos] == "\\":
            if cart.facing == "<":
                cart.x_pos -= 1
                cart.facing = "^"
            elif cart.facing == "v":
                cart.y_pos += 1
                cart.facing = ">"
            elif cart.facing == ">":
                cart.x_pos += 1
                cart.facing = "v"
            elif cart.facing == "^":
                cart.y_pos -= 1
                cart.facing = "<"

        # check if the cart collides with another cart
        for c in carts:
            if c.x_pos == cart.x_pos and c.y_pos == cart.y_pos:
                if c != cart:
                    collision = True
                    print("collision at X: " + str(cart.y_pos) + " Y: " + str(cart.x_pos))
                    colliding_carts.append(cart)
                    colliding_carts.append(c)
    for col in colliding_carts:
        carts.remove(col)
    return collision


def turn_cart(cart):
    if cart.facing == ">":
        if cart.next_turn == "left":
            cart.facing = "^"
            cart.x_pos -= 1
            cart.next_turn = "straight"
        elif cart.next_turn == "right":
            cart.facing = "v"
            cart.x_pos += 1
            cart.next_turn = "left"
        else:
            cart.next_turn = "right"
            cart.y_pos += 1
    elif cart.facing == "<":
        if cart.next_turn == "left":
            cart.facing = "v"
            cart.x_pos += 1
            cart.next_turn = "straight"
        elif cart.next_turn == "right":
            cart.facing = "^"
            cart.x_pos -= 1
            cart.next_turn = "left"
        else:
            cart.next_turn = "right"
            cart.y_pos -= 1
    elif cart.facing == "^":
        if cart.next_turn == "left":
            cart.facing = "<"
            cart.y_pos -= 1
            cart.next_turn = "straight"
        elif cart.next_turn == "right":
            cart.facing = ">"
            cart.y_pos += 1
            cart.next_turn = "left"
        else:
            cart.next_turn = "right"
            cart.x_pos -= 1
    elif cart.facing == "v":
        if cart.next_turn == "left":
            cart.facing = ">"
            cart.y_pos += 1
            cart.next_turn = "straight"
        elif cart.next_turn == "right":
            cart.facing = "<"
            cart.y_pos -= 1
            cart.next_turn = "left"
        else:
            cart.next_turn = "right"
            cart.x_pos += 1


def draw_tracks(track, carts):

    for x in range(len(track)):
        line = ""
        for y in range(len(track[0])):
            cart = False
            for c in carts:
                if c.x_pos == x and c.y_pos == y:
                    line += c.facing
                    cart = True
                    break
            if not cart:
                line += lines[x][y]
        print(line)

f = open("input13.txt", "r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")


carts = []

# lets find carts
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == "v" or lines[x][y] == "^" or lines[x][y] == "<" or lines[x][y] == ">":
            carts.append(Cart(lines[x][y], x, y))
    lines[x] = lines[x].replace(">", "-")
    lines[x] = lines[x].replace("<", "-")
    lines[x] = lines[x].replace("v", "|")
    lines[x] = lines[x].replace("^", "|")

while len(carts) > 1:
    # draw_tracks(lines, carts)
    move_carts(lines, carts)
print("one car left at X:" + str(carts[0].y_pos) + " Y: " + str(carts[0].x_pos))
