def checksum():
    f = open("input2.txt", "r")
    lines = f.readlines()

    doubleDigits = 0
    tripleDigits = 0
    for line in lines:
        # print(line)
        counter = 0
        sortedLine = sorted(line)

        double = False
        triple = False

        for j in range(len(sortedLine)-1):
            if sortedLine[j] == sortedLine[j+1]:
                counter += 1

            else:
                if counter == 2 and not triple:
                    tripleDigits += 1
                    triple = True
                    # print("found triple!")
                if counter == 1 and not double:
                    doubleDigits += 1
                    double = True
                    # print("found double!")
                counter = 0
        # we must also check doubles and triples after last character
        if counter == 2 and not triple:
            tripleDigits += 1
            # print("found triple!")
        if counter == 1 and not double:
            doubleDigits += 1
            # print("found double!")

    print("Double digits: " + str(doubleDigits))
    print("Triple digits: " + str(tripleDigits))
    print("Checksum is: " + str(tripleDigits * doubleDigits))


def correct_box():
    f = open("input2.txt", "r")
    lines = f.readlines()
    answer = ""
    for i, line in enumerate(lines):
        for j, line2 in enumerate(lines):
            differences = 0
            for k, character in enumerate(line):
                if character != line2[k]:
                    differences += 1
            if differences == 1:
                print("Similar boxes are:" + "\n" + line + "and" + "\n" + line2)
                for c in range(len(line)):
                    if line[c] != line2[c]:
                        answer = line[:c] + line[c+1:]
                print("Common characters are: " + answer)
                return


checksum()
correct_box()
