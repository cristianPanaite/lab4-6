from math import sqrt


def set_number(x, y):
    return [x, y]


def get_real(c):
    return c[0]


def get_immaginary(c):
    return c[1]


def set_number_from_string(s):
    s = s.replace(" ", "")
    b = complex(s)
    return set_number(b.real, b.imag)


def toString(c):
    a = get_real(c)
    b = get_immaginary(c)

    if a == 0:
        return "{}i".format(b)
    elif b == 0:
        return "{}".format(a)
    elif b > 0:
        return "{} + {}i".format(a, b)
    else:
        return "{} - {}i".format(a, b * -1)


def clona_numar(c):
    return [c[0], c[1]]


def module(c):
    return sqrt(get_real(c) * get_real(c) + get_immaginary(c) * get_immaginary(c))


def sum_of_2_numbers(c1, c2):
    real = get_real(c1) + get_real(c2)
    imag = get_immaginary(c1) + get_immaginary(c2)

    c3 = set_number(real, imag)
    return c3


def product_of_2_numbers(c1, c2):
    # product of 2 numbers
    a = get_real(c1)
    b = get_immaginary(c1)
    c = get_real(c2)
    d = get_immaginary(c2)

    return set_number((a * c - b * d), (a * d + b * c))
