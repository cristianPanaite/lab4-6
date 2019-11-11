from services import *

def toInt(a):

    # functia verifica daca input-ul e numar si citeste pana cand e un numar
    # a - string

    while True:
        try:
            a = int(a)
            return a
        except ValueError:
            a = input("Please insert an integer : ")


def indexOutOfRangeError(ind, currentList):

    # verifica daca indicele citit este in dimensiunea listei
    # ind - integer
    # currentList - lista

    while ind > len(currentList):
        ind = input("The index is out of range. Please reinsert one: ")
        ind = toInt(ind)
    return ind


def emptyListError(currentList):

    # functie care verifica daca lista e goala
    # currentList - lista

    if len(currentList) == 0:
        print("The list is empty")
        return True
    return False


def goodInterval(indStart, indFin, currentList):
    # verifica daca intervalul dat de indicii indStart si indFin e valid
    # indStart, indFin - integer
    # currentList - lista

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