
import itertools
import re

def checkDecrease(number):
    result = all(x <= y for x, y in zip(list(number), list(number)[1:]))

    return result

def checkDoubles(number):
    result = any(x == y for x, y in zip(list(number), list(number)[1:]))

    return result

def checkPartOfGroup(number):
    doublesList = []
    for x, y in zip(list(number), list(number)[1:]):
        if x == y:
            doublesList.append("{}{}".format(x,y))

    checkList = []
    for doubles in doublesList:

        coordinates = [m.start() for m in re.finditer(doubles, number)]

        for coords in coordinates:
            if coords == 4:
                if number[coords - 1] == number[coords] == number[coords + 1]:
                    checkList.append(True)
                elif number[coords] == number[coords + 1]:
                    checkList.append(False)
            
            elif number[coords] == number[coords + 2]:
                checkList.append(True)
            else:
                checkList.append(False)

    if False in checkList:
        return False
    else:
        return True


totalList = []

for password in range(130254, 678275):
    password = str(password)

    if (checkDoubles  (password)   == True and
        checkDecrease (password)   == True and
        checkPartOfGroup(password) == False):

        totalList.append(password)
print(len(totalList))
