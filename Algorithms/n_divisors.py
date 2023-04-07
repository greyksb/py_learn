#https://math.stackexchange.com/questions/2754556/smallest-number-with-at-least-n-divisors
import math
import time


def mp_divisor_count(n):
    count = 1
    i = 2
    while i < n + 1:
        p = 0
        while n % i == 0:
            n /= i
            p += 1
        count *= (p + 1)
        i += 1
    return count


# def mp_factored(n):
#     factors = []
#     i = 2
#     while i < n + 1:
#         if n % i == 0:
#             factors.append(i)
#             n /= i
#         else:
#             i += 1
#     return factors


def to_power(base, exponent):
    return math.pow(base, exponent)


def find_min_n(d):
    lst = []
    for e2 in range(24):
        for e3 in range(e2 + 1):
            for e5 in range(e3 + 1):
                for e7 in range(e5 + 1):
                    for e11 in range(e7 + 1):
                        for e13 in range(e11 + 1):
                            for e17 in range(e13 + 1):
                                n = to_power(2, e2)
                                n *= to_power(3, e3)
                                n *= to_power(5, e5)
                                n *= to_power(7, e7)
                                n *= to_power(11, e11)
                                n *= to_power(13, e13)
                                n *= to_power(17, e17)
                                if n < 10_000_000:
                                    mpc = mp_divisor_count(n)
                                    lst.append([mpc, n])

    lst.sort()
    for i in range(0, len(lst)):
        if d == int(lst[i][0]):
            return int(lst[i][1])
    return None


st = time.time()
print(find_min_n(420))
et = time.time()
print(f"work time is {et-st:.4}")