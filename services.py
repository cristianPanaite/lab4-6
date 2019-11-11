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

def takeCmdList(listofcommands, pageName, currentList, undoList):
    # function that parse the command
    print("{} Menu".format(pageName))
    print('Type "help" to find out what functions you can call')
    cmd = input(">>>")
    str = cmd.split()
    return str

def copy_to_undo_list(list):
    #functie care returneaza o copie a unei liste

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
    #functie care sterge un element de pe o pozitie

    del list[poz]
    return list


def delete_range_element(istart, ifin, list):

    # functie care sterge elementele de pe un interval

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
    # returneaza lista cu partea imaginara a elementelor de pe un anumit interval

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
    # efectueaza suma pe un anumit interval dat

    rez = set_number(0, 0)
    for i in list[start:finish]:
        rez = sum_of_2_numbers(rez, i)
    return rez


def interval_product(start, finish, list):
    # product of complex numbers
    rez = set_number(1, 1)

    for number in list[start:finish]:
        rez = product_of_2_numbers(rez, number)

    return rez


def sortedDesc(list):
    # function that sort a list
    retList = list[:]
    retList.sort(key=lambda x: x[1], reverse=True)  # by second argument

    return retList


def take_not_primes_numbers(list):
    # returneaza lista cu numerele care nu au partea intreaga prima

    out = []
    for c in list:
        if not real_part_prime(c):
            out.append(c)
    return out


def take_number(key):
    # taking a int number from the user data

    a = input("Please insert the {} : ".format(key))
    return toInt(a)


def module_less(list, number):

    # returneaza lista cu numerele care au modulul mai mic decat un numar

    l = []
    for c in list:
        if module(c) < number:
            l.append(c)

    return l


def module_equal(list, number):
    # returneaza lista cu numerele care au modulul egal cu un numar

    l = []
    for c in list:
        if module(c) == number:
            l.append(c)

    return l


def module_grater(list, number):
    # returneaza lista cu numerele care au modulul mai mare decat un numar
    l = []
    for c in list:
        if module(c) > number:
            l.append(c)

    return l


def do_the_undo(list, undo_l):
    new = copy_to_undo_list(undo_l[len(undo_l) - 1])
    undo_l.pop()
    return new