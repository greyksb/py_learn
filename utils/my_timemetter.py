import time

def timemetter(some_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = some_func(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f'function {some_func.__name__} ended...  time working is: {delta_time:.4}')
        return res
    return wrapper


def test_tm():
    def test_func(n):
        lst = []
        for i in range(n):
            lst.append(i)

    def test_func2(n):
        lst = n*[0]
        for i in range(n):
            lst[i] = i
    test_func = timemetter(test_func)
    test_func2 = timemetter(test_func2)
    N = 1_000_000
    print(f'test for {N} iteration')
    test_func(N)
    test_func2(N)


if __name__ == '__main__':
    test_tm()
