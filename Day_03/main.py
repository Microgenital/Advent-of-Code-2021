#############################
# www.adventofcode.com/2021 #
#     Challenge: Day 3      #
#############################

def main_01():
    # read input data from input.txt
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    # all strings have the same length, get the length of the first string
    length = len(data[0])

    gammaRate = ""
    epsilonRate = ""

    sum0 = 0
    sum1 = 0

    # loop over all strings
    for j in range(length):
        for i in range(len(data)):
            if data[i][j] == "1":
                sum1 += 1
            elif data[i][j] == "0":
                sum0 += 1
        if sum1 > sum0:
            gammaRate += "1"
            epsilonRate += "0"
        elif sum1 < sum0:
            gammaRate += "0"
            epsilonRate += "1"

        sum0 = 0
        sum1 = 0

    print("Gamma rate:", gammaRate, "in decimal:", int(gammaRate, 2))
    print("Epsilon rate:", epsilonRate, "in decimal:", int(epsilonRate, 2))

    print("final solution:", int(gammaRate, 2) * int(epsilonRate, 2))


def main_02():
    # read input data from input.txt
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    # all strings have the same length, get the length of the first string
    length = len(data[0])

    # copy the list to new list to be able to modify it without changing the original list
    oxygenGeneratorRating = data[:]
    co2ScrubberRating = data[:]

    sum0 = 0
    sum1 = 0
    toDeleteOxygen = []
    toDeleteCo2 = []

    # loop over all strings
    for column in range(length):
        if len(oxygenGeneratorRating) > 1:
            for row in range(len(oxygenGeneratorRating)):
                if oxygenGeneratorRating[row][column] == "1":
                    sum1 += 1
                else:
                    sum0 += 1

            print(f"sum1: {sum1}, sum0: {sum0}")
            if sum1 > sum0:
                for row in range(len(oxygenGeneratorRating)):
                    if oxygenGeneratorRating[row][column] == "0":
                        toDeleteOxygen.append(row)
                    else:
                        continue

            elif sum1 < sum0:
                for row in range(len(oxygenGeneratorRating)):
                    if oxygenGeneratorRating[row][column] == "1":
                        toDeleteOxygen.append(row)
                    else:
                        continue

            elif sum1 == sum0:
                for row in range(len(oxygenGeneratorRating)):
                    if oxygenGeneratorRating[row][column] == "0":
                        toDeleteOxygen.append(row)
                    else:
                        continue

            toDeleteOxygen.reverse()

            for i in toDeleteOxygen:
                del oxygenGeneratorRating[i]

            toDeleteOxygen = []
            sum0 = 0
            sum1 = 0
        else:
            break


    for column in range(length):
        if len(co2ScrubberRating) > 1:
            for row in range(len(co2ScrubberRating)):
                if co2ScrubberRating[row][column] == "1":
                    sum1 += 1
                else:
                    sum0 += 1

            print(f"sum1: {sum1}, sum0: {sum0}")
            if sum1 < sum0:
                for row in range(len(co2ScrubberRating)):
                    if co2ScrubberRating[row][column] == "0":
                        toDeleteCo2.append(row)
                    else:
                        continue

            elif sum1 > sum0:
                for row in range(len(co2ScrubberRating)):
                    if co2ScrubberRating[row][column] == "1":
                        toDeleteCo2.append(row)
                    else:
                        continue
            elif sum1 == sum0:
                for row in range(len(co2ScrubberRating)):
                    if co2ScrubberRating[row][column] == "1":
                        toDeleteCo2.append(row)
                    else:
                        continue

            toDeleteCo2.reverse()

            for i in toDeleteCo2:
                del co2ScrubberRating[i]

            toDeleteCo2 = []
            sum0 = 0
            sum1 = 0
        else:
            break

    print("Oxygen generator rating:", oxygenGeneratorRating)
    print("CO2 scrubber rating:", co2ScrubberRating)
    print("final solution:", int(oxygenGeneratorRating[0], 2) * int(co2ScrubberRating[0], 2))


if __name__ == "__main__":
    main_02()
