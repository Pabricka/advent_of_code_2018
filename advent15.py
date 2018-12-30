class Tile:

    def __init__(self, tile_type, x, y):
        self.tile_type = tile_type
        self.x = x
        self.y = y

    def __str__(self):
        return self.tile_type


class Unit:

    def __init__(self, unit_type, x, y, buff):
        self.unit_type = unit_type
        self.x = x
        self.y = y
        self.hp = 200
        self.attack_power = 3 + buff

    def __str__(self):
        return self.unit_type


def next_turn(elves_can_die):
    copy_of_units = sorted(units, key=lambda u: (u.y, u.x))
    for unit in copy_of_units:
        if unit.hp > 0:
            attacked = attack(unit, elves_can_die)
            if attacked == "Game over":
                return True
            if attacked == "Elves win":
                return "Elves win"
            if attacked == "Elf died":
                return "Elf died"
            if not attacked:
                m = find_path(unit)
                if m is not None:
                    move_to(unit, m[0])
                    attack(unit, elves_can_die)
    return False


def attack(unit, elves_can_die):
    enemy = "G"
    if unit.unit_type == "G":
        enemy = "E"
    adjacent_tiles = get_neighbours(unit)
    enemies = []
    for tile in adjacent_tiles:
        if str(tile) == enemy:
            enemies.append(tile)
    if len(enemies) > 0:
        lowest_hp = min(enemies, key=lambda x: x.hp)
        target = enemies[0]
        for e in enemies:
            if e.hp == lowest_hp.hp:
                target = e
                break
        target.hp -= unit.attack_power
        if target.hp <= 0:
            if not elves_can_die:
                if target.unit_type == "E":
                    return "Elf died"
            area[target.x][target.y] = Tile(".", target.x, target.y)
            units.remove(target)
            elves = 0
            goblins = 0
            for u in units:
                if u.unit_type == "G":
                    goblins += 1
                else:
                    elves += 1
            if elves == 0:
                print("All elves are dead :( Combined HP of remaining units:")
                combined_hp_of_remaining_units = sum(map(lambda x: x.hp, units))
                print(combined_hp_of_remaining_units)
                draw_area()
                return "Game over"
            if goblins == 0:
                print("All goblins are dead :) Combined HP of remaining units:")
                combined_hp_of_remaining_units = sum(map(lambda x: x.hp, units))
                print(combined_hp_of_remaining_units)
                draw_area()
                return "Elves win"
        return True
    return False


def get_neighbours(unit):
    return [area[unit.x][unit.y-1], area[unit.x-1][unit.y], area[unit.x+1][unit.y], area[unit.x][unit.y+1]]


def move_to(unit, to):
    tmp_x = to.x
    tmp_y = to.y
    to.x = unit.x
    to.y = unit.y
    area[unit.x][unit.y] = to
    unit.x = tmp_x
    unit.y = tmp_y
    area[tmp_x][tmp_y] = unit


# breadth-first search to determine where to move next
def find_path(unit):

    enemy = "G"
    if unit.unit_type == "G":
        enemy = "E"
    first_moves = []
    for m in get_neighbours(unit):
        if isinstance(m, Tile) and m.tile_type == ".":
            first_moves.append(m)
    best_moves = []
    for move in first_moves:
        stack = []
        for n in get_neighbours(move):
            if isinstance(n, Unit) and n.unit_type == enemy:
                best_moves.append([move, 1, move])
            elif isinstance(n, Tile) and n.tile_type == ".":
                stack.append(n)
        seen = set()
        seen.add(unit)
        seen.add(move)
        i = 1
        run = True
        while run:
            i += 1
            new_stack = []

            for s in stack:
                if s in seen:
                    continue

                seen.add(s)
                for n in get_neighbours(s):
                    if isinstance(n, Unit) and n.unit_type == enemy:
                        best_moves.append([move, i, s])
                        run = False
                        continue

                for n in get_neighbours(s):
                    if isinstance(n, Tile) and n.tile_type == "." and n not in seen:
                        new_stack.append(n)
            stack = list(set(new_stack))
            if not stack:
                run = False
    if best_moves:
        # First condition - fewest number of moves away
        min_steps = min([x[1] for x in best_moves])
        best_moves = [x for x in best_moves if x[1] == min_steps]

        # Second condition - if tie, choose the first tile in reading order
        best_moves.sort(key=lambda x: (x[2].y, x[2].x))
        best_moves = [x for x in best_moves if x[2] == best_moves[0][2]]

        # Third condition - if tie, take the first step in reading order
        best_moves.sort(key=lambda x: (x[0].y, x[0].x))
        best_moves = [x for x in best_moves if x[0] == best_moves[0][0]]

        return best_moves[0]
    else:
        return None


def draw_area():
    for y in range(len(area)):
        line = ""
        hp_line = " "
        for x in range(len(area[0])):
            line += str(area[x][y])
            if isinstance(area[x][y], Unit):
                hp_line += "(" + str(area[x][y].hp) + ")"
        print(line + hp_line)


def read_input(buff):
    f = open("input15.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        area.append([])
        for j in range(len(lines[0].strip("\n"))):
            if lines[j][i] == "G":
                u = Unit("G", i, j, 0)
                units.append(u)
                area[i].append(u)
            elif lines[j][i] == "E":
                u = Unit("E", i, j, buff)
                units.append(u)
                area[i].append(u)
            else:
                area[i].append(Tile(lines[j][i], i, j))


area = []
units = []
read_input(0)

# part 1
end = False
i = 0
elves_can_die = True
while not end:
    print("Turn " + str(i))
    i += 1
    #draw_area()
    end = next_turn(elves_can_die)
    if end == "Elves win":
        break

# part 2
end = False
buff = 0
elves_can_die = False
while end != "Elves win":
    i = 0
    buff += 1
    area = []
    units = []
    read_input(buff)
    print("Buffing elves with +" + str(buff) + " attack power...")
    end = False
    while not end:
        print("Turn " + str(i))
        i += 1
        # draw_area()
        end = next_turn(elves_can_die)
        if end == "Elves win":
            break
        elif end == "Elf died":
            break
