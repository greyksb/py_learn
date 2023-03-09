# a function for finding the number of combinations from n by k
import math

def combinations(n: int, k: int) -> int:
    """
    a function for finding the number of combinations from n by k
    """
    if n < k:
        return -1
    else:
        return round(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) 


if __name__ == '__main__':

# uncomment for texting combinations()
    print(combinations.__doc__)
    n = 5
    k = 3
    print(combinations(n, k))
