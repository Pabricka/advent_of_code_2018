recipes = "37"
first_elf = 0
second_elf = 1

sequence = "556061"
found = False
while sequence not in recipes[-7:]:
    first_score = int(recipes[first_elf])
    second_score = int(recipes[second_elf])
    recipes += str(first_score + second_score)
    for a in range(first_score + 1):
        if first_elf < len(recipes)-1:
            first_elf += 1
        else:
            first_elf = 0
    for a in range(second_score + 1):
        if second_elf < len(recipes)-1:
            second_elf += 1
        else:
            second_elf = 0

# part 1
print(recipes[int(sequence):int(sequence)+10])

# part 2
print(recipes.index(sequence))
