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
    pass


if __name__ == "__main__":
    main_01()
