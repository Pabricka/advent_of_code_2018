def largest_power_fuel_cell(serial_number):

    grid = [[0 for i in range(300)]for j in range(300)]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            rack_id = x+11
            power = rack_id*(y+1)
            power += serial_number
            power *= rack_id
            power_str = str(power)
            if len(power_str) >= 3:
                power = int(power_str[len(power_str) - 3])
            else:
                power = 0
            power -= 5
            grid[x][y] = power

    largest = 0
    largest_x = 0
    largest_y = 0
    for x in range(len(grid)-2):
        for y in range(len(grid[0])-2):
            total = 0
            for i in range(3):
                for j in range(3):
                    total += grid[x + i][y + j]
                if total > largest:
                    largest = total
                    largest_x = x
                    largest_y = y
                    print("largest now: " + str(largest))

    print("X: " + str(largest_x+1) + " Y: " + str(largest_y+1))
    return largest_x, largest_y


serial = 6548
largest_power_fuel_cell(serial)
