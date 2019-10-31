from services import take_number

def toInt(a):
    while True:
        try:
            a = int(a)
            return a
        except ValueError:
            a = input("Please insert an integer : ")


def indexOutOfRangeError(ind, currentList):
    while ind > len(currentList):
        ind = input("The index is out of range. Please reinsert one: ")
        ind = toInt(ind)
    return ind


def emptyListError(currentList):
    if len(currentList) == 0:
        print("The list is empty")
        return True
    return False


def goodInterval(indStart, indFin, currentList):
    indStart = take_number("Start Index")
    indStart = indexOutOfRangeError(indStart, currentList)
    indFin = take_number("Finish Index")
    indFin = indexOutOfRangeError(indFin, currentList)
    while indStart > indFin:  # verify a <= b, (a, b) interval
        print("Incorrect values. Start index bigger than Finish index. Please reinsert!")
        indStart = take_number("Start Index")
        indStart = indexOutOfRangeError(indStart, currentList)
        indFin = take_number("Finish Index")
        indFin = indexOutOfRangeError(indFin, currentList)

    return [indStart, indFin]