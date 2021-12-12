#############################
# www.adventofcode.com/2021 #
#     Challenge: Day 1      #
#          Part 1           #
#         Solution:         #
#           1167            #
#############################


def main_01():
    # read input data from input.txt
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    # convert input strings to ints
    intData = [int(x) for x in data]

    # count the incremental changes
    increments = 0
    listLength = len(intData)

    # check if data is higher than the last element
    for i in range(listLength - 1):
        # if data is higher than the last element, starting with the second element, increase the increments
        if intData[i + 1] > intData[i]:
            increments += 1

    print(increments)


def main_02():
    # read input data from input.txt
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    # convert input strings to ints
    intData = [int(x) for x in data]

    # count the incremental changess
    increments = 0
    listLength = len(intData)

    # take the sum of the first 3 entrys, and compate to the next 3 entrys
    index_1 = 0
    index_2 = 1
    index_3 = 2

    while index_3 < listLength - 1:
        compared_1 = intData[index_1] + intData[index_2] + intData[index_3]

        index_1 += 1
        index_2 += 1
        index_3 += 1

        compared_2 = intData[index_1] + intData[index_2] + intData[index_3]

        if compared_2 > compared_1:
            increments += 1

    print(increments)


if __name__ == "__main__":
    main_02()
