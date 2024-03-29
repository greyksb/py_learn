import random
import itertools
def lrn_match(n):
    zero = odd_num = even_num = errors = 0
    res = 10 * [0]
    for i in range(n):
        flag = True
        rnd_num = random.randint(-1, 12)
        match rnd_num:
            case 0:
                zero += 1
            case 1 | 3 | 5 | 7 | 9:
                odd_num += 1
            case 2 | 4 | 6 | 8:
                even_num += 1
            case _:
                flag = False
                errors += 1
                #print("Error: out of range!!! ")
        if flag:
            res[rnd_num] += 1

    print(res)
    print("in range 0 - 9 : ", sum(res))
    print("out of range : ", errors)


def default_args1(x, lst=[]):
    lst.append(x)
    return lst


def default_args2(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst


def lrn_default_args():
    for n in range(8):
        print(default_args1(n))
    print('-------------------------')
    some_list = [-1, -2]
    for n in range(8):
        print(default_args1(n, some_list))
    print('-------------------------')
    for n in range(8):
        print(default_args2(n))
    print('-------------------------')
    some_list = [-1, -2]
    for n in range(8):
        print(default_args2(n, some_list))

def build_list(n):
    lst = [1]
    for i in range(n):
        x = lst[i]*2+1
        if x not in lst:
            lst += [x]
        x = lst[i]*3+1
        if x not in lst:
            lst += [x]
    return lst

def func(p, n):
    if p[-1] == n:
        return p
    else:
        p += n
        return p

def test_accumulate(s):
    return list(itertools.accumulate(s, func))[-1]


def add_to_list(*x, a=None):
    if a is None:
        a = []
    for e in x:
        a.append(e)
    return a


def test_add_to_list():
    lst = []
    add_to_list(1, a=lst)
    add_to_list(2, a=lst)
    add_to_list(3, a=lst)
    print(lst)
    lst = add_to_list(1)
    print(lst)
    lst = add_to_list(1, 2, 3, 4)
    print(lst)


if __name__ == '__main__':
    # как работает аналог switch(){ case}  в Python
    #lrn_match(1000)
    # аргументы по умолчанию
    #lrn_default_args()
    #print(*build_list(10))
    #print(test_accumulate("rrrrrrrretturnnnnnnnnnnnnnnnnn"))
    test_add_to_list()
