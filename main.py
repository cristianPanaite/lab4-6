from ui_module import ui_project
from tests import run_tests


def run():
    list_complex = []  # main list
    undoList = []
    run_tests()
    ui_project(list_complex, undoList) # start ui function


run()
