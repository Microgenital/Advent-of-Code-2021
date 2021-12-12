#############################
# www.adventofcode.com/2021 #
#     Challenge: Day 2      #
#############################

def main_01():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        # get the data and split it into a list of strings
        strData = [(x) for x in data]

    # set starting values
    horizontalPos = 0
    depthPos = 0

    # set commands
    forward = "forward"
    down = "down"
    up = "up"


    # loop through the list of strings
    for i in range(len(strData)):
        if forward in strData[i]:
            horizontalPos += int(strData[i][-1:])
        elif down in strData[i]:
            depthPos += int(strData[i][-1:])
        elif up in strData[i]:
            depthPos -= int(strData[i][-1:])
        else:
            continue

    print("The final horizontal position is: " + str(horizontalPos))
    print("The final depth position is: " + str(depthPos))

    final_solution = horizontalPos * depthPos
    print("The final solution is: " + str(final_solution))


if __name__ == "__main__":
    main_01()
