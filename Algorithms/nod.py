# Алгоритмы нахождения наибольшего общего делителя
from my_timemetter import timemetter as tm
def fast_euclide_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def slow_euclide_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

if __name__ == '__main__':
    fast_euclide_nod = tm(fast_euclide_nod)
    slow_euclide_nod = tm(slow_euclide_nod)

    print(fast_euclide_nod(81000000003600, 12306000000003600))
    print(slow_euclide_nod(81000000003600, 12306000000003600))
