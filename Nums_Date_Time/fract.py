from fractions import Fraction
def fract():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    print(a+b)
    c = a + b                           # or *, -, /
    print(c.numerator, c.denominator)
    print(format(float(c), '0.3'))


if __name__ == '__main__':
    fract()
