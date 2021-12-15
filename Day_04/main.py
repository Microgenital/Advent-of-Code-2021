#############################
# www.adventofcode.com/2021 #
#     Challenge: Day 4      #
#############################

def main_01():
    with open('input_demo.txt', 'r') as f:
        data = f.read().splitlines()

    # Get the bingo numbers from the input and convert them to integers
    bingoNumbers = data[0].split(',')
    bingoNumbers = [int(x) for x in bingoNumbers]
    del data[0]

    data = [x.split() for x in data]
    bingoBoards = data[:]

    delete = []
    for i in range(len(bingoBoards)):
        if len(bingoBoards[i]) != 5:
            delete.append(i)
    for i in reversed(delete):
        del bingoBoards[i]

    # convert the bingo boards to integers
    for i in range(len(bingoBoards)):
        for j in range(len(bingoBoards[i])):
            bingoBoards[i][j] = int(bingoBoards[i][j])

    # create for every 5 elements a new list
    bingoBoards = [bingoBoards[i:i + 5] for i in range(0, len(bingoBoards), 5)]
    print(bingoBoards)

    # Todo: loop through the bingoBoards and check if the numbers are in the bingoBoards


def main_02():
    pass


if __name__ == "__main__":
    main_01()
