def count_even_dits(n: int) -> int:
    """
    количество четных цифр в числе
    """
    # cnt = 0
    # for digit in list(str(abs(n))):
    #     if int(digit) % 2 == 0:
    #         cnt += 1
    # return cnt

    return sum(x in '02468' for x in str(n))


def is_prime(num: int) -> bool:
    """
    Оптимизированный алгоритм поиска простых неотрицательных чисел:

    проверить на 0 и 1
    проверить на чётность и равенство 2 (исключается ~50% чисел)
    проверить на кратность 3 и равенство 3 (исключается ещё ~33% чисел)
    для проверки оставшихся чисел воспользоваться формулой 6n ± 1
    (при n = 1, простыми будут 5 и 7, при n = 2: 11 и 13, и т.д.)
    проверять делители следует до корня из заданного числа
    """
    isprime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)

    i = 5
    d = 2

    while isprime and i * i <= num:
        isprime = num % i != 0
        i += d
        d = 6 - d                       # чередование прироста 2 и 4: 5 + 2, 7 + 4, 11 + 2, и т.д.
    return isprime



def fnd_max_prime(n :int) -> int:
    #max_even_digits = max([count_even_dits(x) for x in range(n, n//10, -1) if is_prime(x) and count_even_dits(x) > 0])
    max_even_digits = len(str(n-1))-1
    if str(n-1)[0] == '1':
        max_even_digits -= 1
    if max_even_digits <= 0:
        max_even_digits = 1
    result = None
    for e in range(n-1, 0, -1):
        if is_prime(e) and count_even_dits(e) >= max_even_digits:
            result = e
            break
    return result


if __name__ == '__main__':
    #print(is_prime(8887))
    #print(count_even_dits(102))
    print(fnd_max_prime(1210))
