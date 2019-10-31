from complexModel import *
from math import sqrt
from services import *

def moduleTest():
    #   testing module
    c = (5, 4)
    assert (module(c) == sqrt(25 + 16))
    c = (5, -3)
    assert (module(c) == sqrt(25 + 9))
    c = (0, 0)
    assert (module(c) == 0)

def deletetest():
    l = [[3.0, 2.0], [4.0, 5.0], [3, 0]]

    assert (delete_an_element(0, l) == [[4.0, 5.0], [3, 0]])

def changeElementTest():
    l = [[3.0, 2.0], [4.0, 5.0], [3, 0], [3.0, 2.0]]

    assert (changeElement(3, 2, 3, 3, l) == [[3, 3],[4.0, 5.0], [3, 0], [3, 3]])

def sumTest():
    c1 = set_number_from_string("5+6j")
    c2 = set_number_from_string("7+8j")
    assert (sum_of_2_numbers(c1, c2) == [12, 14])

    c1 = set_number_from_string("5+6j")
    c2 = set_number_from_string("-5-6j")
    assert (sum_of_2_numbers(c1, c2) == [0, 0])

    c1 = set_number_from_string("5+6j")
    c2 = set_number_from_string("-5+8j")
    assert (sum_of_2_numbers(c1, c2) == [0, 14])

    c1 = set_number_from_string("5+6j")
    c2 = set_number_from_string("-6+6j")
    assert (sum_of_2_numbers(c1, c2) == [-1, 12])


def run_tests():
    deletetest()
    sumTest()
    changeElementTest()
    moduleTest()