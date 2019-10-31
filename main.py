from tests import *
from services import *
from errors import *


def ui_add_insert(list, undo_l):
    undo_l.append(copy_to_undo_list(list))

    poz = take_number('index')
    while True:
        s = input("insert complex number: ")
        try:
            c = set_number_from_string(s)
            add_to_list(c, list, poz)
            return
        except:
            print("Nu ai introdus un numar complex. Mai incearca")


def ui_add_at_finish(list, undo_l):
    undo_l.append(copy_to_undo_list(list))

    while True:

        s = input("insert complex number: ")
        try:
            c = set_number_from_string(s)
            add_to_list(c, list, -1)
            return
        except:
            print("Nu ai introdus un numar complex. Mai incearca")


def ui_add(list, undo_l):
    addComands = {
        "finish": ui_add_at_finish,
        "insert": ui_add_insert,
        "help": ui_help,
    }

    while True:
        cmd = takeCmd(addComands, "Add", list, undo_l)
        if cmd == 'exit':
            return
        if cmd in addComands:
            if cmd == 'help':
                addComands[cmd](addComands)
            else:
                addComands[cmd](list, undo_l)
        else:
            print("comanda introdusa nu se afla printre cele posibile")


def ui_deleteAnElement(list, undo_l):
    # ui function to delete a specific element (on an index entered by user)
    undo_l.append(copy_to_undo_list(list))

    poz = take_number('index')
    poz = indexOutOfRangeError(poz, list)
    if emptyListError(list):
        return
    delete_an_element(poz, list)

def ui_rangeDelete(list, undo_l):
    # ui function to delete an interval

    undo_l.append(copy_to_undo_list(list))
    if emptyListError(list) == True:
        return
    indStart = take_number("Start Index")
    indStart = indexOutOfRangeError(indStart, list)
    indFin = take_number("Finish Index")
    indFin = indexOutOfRangeError(indFin, list)
    while indStart > indFin:  # verify a <= b, (a, b) interval
        print("Incorrect values. Start index bigger than Finish index. Please reinsert!")
        indStart = take_number("Start Index")
        indStart = indexOutOfRangeError(indStart, list)
        indFin = take_number("Finish Index")
        indFin = indexOutOfRangeError(indFin, list)
    delete_range_element(indStart, indFin, list)

def ui_change(list, undo_l):
    # ui function to change elements (2.c.)
    undo_l.append(copy_to_undo_list(list))
    a = take_number("real part")
    b = take_number("imaginary part")
    aa = take_number("real part to change")
    bb = take_number("imaginary part to change")

    changeElement(a, b, aa, bb, list)

def ui_modify(list, undo_l):
    modifyComands = {
        "delIndex": ui_deleteAnElement,
        "rangeDel": ui_rangeDelete,
        "changeN": ui_change,
        "help": ui_help
    }

    while True:
        cmd = takeCmd(modifyComands, "Modify", list, undo_l)
        if cmd == 'exit':
            return
        if cmd in modifyComands:
            if cmd == 'help':
                modifyComands[cmd](modifyComands)
            else:
                modifyComands[cmd](list, undo_l)
        else:
            print("comanda introdusa nu se afla printre cele posibile")

def ui_imaginaryPart(list, undo_l):
    # 3.a.

    a = take_number("start index")
    b = take_number("stop index")
    imaginaryPartPrint(a, b, list)

def ui_less10(list, undo_l):
    # 3.b.
    print("Complex numbers that have a module less than 10: ")
    list_less = less10(list)
    ui_print(list_less, undo_l)

def ui_equal10(list, undo_l):
    # 3.c.
    print("Complex numbers that have a module equal to 10")
    listeq = equal10_print(list)
    ui_print(listeq, undo_l)

def ui_searchNumbers(list, undo_l):
    # 3.
    searchComands = {
        "imaginaryPart": ui_imaginaryPart,
        "less10": ui_less10,
        "equal10": ui_equal10,
        "help": ui_help
    }

    while True:
        cmd = takeCmd(searchComands, "Search", list, undo_l)
        if cmd == 'exit':
            return
        if cmd in searchComands:
            if cmd == 'help':
                searchComands[cmd](searchComands)
            else:
                searchComands[cmd](list, undo_l)
        else:
            print("comanda introdusa nu se afla printre cele posibile")


def ui_sumNum(list, undo_l):
    # 4.a. reads start and finish index
    start = 0
    finish = -1
    indexes = goodInterval(start, finish, list)
    start = indexes[0]
    finish = indexes[1]

    result = interval_sum(start, finish, list)
    print("Result: {} + {}i".format(result[0], result[1]))

def ui_prod(list, undo_l):
    start = 0
    finish = -1
    indexes = goodInterval(start, finish, list)
    start = indexes[0]
    finish = indexes[1]

    result = interval_product(start, finish, list)

    print("Result: {} + {}i".format(result[0], result[1]))

def ui_sort(list, undo_l):
    pass

def ui_operations(list, undo_l):
    # 4. Ui function
    opComands = {
        "sumNum": ui_sumNum,
        "prod": ui_prod,
        "sort": ui_sort,
        "help": ui_help
    }

    while True:
        cmd = takeCmd(opComands, "Search", list, undo_l)
        if cmd == 'exit':
            return
        if cmd in opComands:
            if cmd == 'help':
                opComands[cmd](opComands)
            else:
                opComands[cmd](list, undo_l)
        else:
            print("comanda introdusa nu se afla printre cele posibile")

def ui_help(commandsUi):
    # function that prints the possibles commands in current Ui menu
    for com in commandsUi:
        print("Type {} for {}".format(com, com))
    print("Type exit for exit")


def ui_print(list, undo_l):
    if emptyListError(list):
        return
    for i in list:
        cString = toString(i)
        print(cString)

def ui_project(list, undo_l):
    commands = {
        "add": ui_add,
        "modify": ui_modify,
        "searchNumbers": ui_searchNumbers,
        "operations": ui_operations,
        "print": ui_print,
        "help": ui_help
    }
    while True:
        cmd = takeCmd(commands, "Start", list, undo_l)
        if cmd == 'exit':
            return
        if cmd in commands:
            if cmd == 'help':
                commands[cmd](commands)
            else:
                commands[cmd](list, undo_l)
        else:
            print("comanda introdusa nu se afla printre cele posibile")


def run():
    list_complex = []
    undoList = []
    run_tests()
    ui_project(list_complex, undoList)


run()
