from complexModel import *
from errors import *


def takeCmd(listofcommands, pageName, currentList, undoList):
    # function that parse the command
    print("{} Menu".format(pageName))
    print('Type "help" to find out what functions you can call')
    cmd = input(">>>")
    if cmd == 'exit':
        return "exit"
    if cmd in listofcommands:
        return cmd
    return "Incorrect command! Please try again"


def copy_to_undo_list(list):
    l = []
    for x in list:
        l.append(clona_numar(x))
    return l


def add_at_finish(c, cList):
    # add an element to the end of list

    cList.append(c)
    return cList


def insert_to_list(pos, c, cList):
    # insert an element on a specific position

    pos = indexOutOfRangeError(pos, cList)  # verify if the index is in range

    cList.insert(pos, c)


def add_to_list(c, cList, pos):
    # add to list function at last or in a specific position

    if pos == -1:
        add_at_finish(c, cList)
    else:
        insert_to_list(pos, c, cList)


def delete_an_element(poz, list):
    del list[poz]
    return list

def delete_range_element(istart, ifin, list):
    del list[istart:ifin]
    return list

def changeElement(a, b, aa, bb, list):
    # change all the elements a + bi with aa + bbi

    if (aa == a and bb == b):
        return
    tup = [aa, bb]
    while True:
        try:
            index = list.index([a, b])  # position where it is
            list[index] = tup
        except ValueError:
            return list


def imaginaryPartPrint(a, b, list):
    l = []
    for i in range(a, b):
        print(get_immaginary(list[i]))
        l.append(get_immaginary(list[i]))

    return l

def less10(list):
    printList = []
    for c in list:
        if module(c) < 10:
            printList.append(c)
    return printList


def equal10_print(list):
    printList = []
    for c in list:
        if module(c) < 10:
            printList.append(c)
    return printList

def interval_sum(start, finish, list):
    rez = set_number(0, 0)
    for i in list[start:finish]:
        rez = sum_of_2_numbers(rez, i)
    return rez

def interval_product(start, finish, list):
    pass


def take_number(key):
    # taking a int number from the user data

    a = input("Please insert the {} : ".format(key))
    return toInt(a)