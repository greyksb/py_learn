import collections
import itertools
import time


def get_all_divisors_brute(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n


def get_prime_divisors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def calc_product(iterable):
    acc = 1
    for i in iterable:
        acc *= i
    return acc


def get_all_divisors(n):
    primes = get_prime_divisors(n)

    primes_counted = collections.Counter(primes)

    divisors_exponentiated = [
        [div ** i for i in range(count + 1)]
        for div, count in primes_counted.items()
    ]

    for prime_exp_combination in itertools.product(*divisors_exponentiated):
        yield int(calc_product(prime_exp_combination))

def find_n_with_d_divisors(d):
    for n in itertools.count(1):
        if d == len(list(get_all_divisors(n))):
            return n


if __name__ == '__main__':
    n = 1572864
    start_time = time.time()
    print(len(list(get_all_divisors(n))))
    end_time = time.time()
    delta_time = end_time - start_time
    print(f'function  get_all_divisors ended...  time working is: {delta_time:.4}')

    # start_time = time.time()
    # print(list(get_all_divisors_brute(n)))
    # end_time = time.time()
    # delta_time = end_time - start_time
    # print(f'function  get_all_divisors_brute ended...  time working is: {delta_time:.4}')

