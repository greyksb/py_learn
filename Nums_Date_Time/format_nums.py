def test1(num):
    """
    '[<>^]?width[,]?(.digits)?',
    где width и digits – целые числа, а ? обозначает необязательные части. Тот
    же формат используется в строковом методе format()
    """
    print(num)
    print(format(num, ">20,"))
    print(format(num, ">20.3E"))
    print(format(num, ">20_"))


def bin_oct_hex():
    n = 156
    print(bin(n), '   ', oct(n), '   ', hex(n))
    print(format(n, 'b'), '   ', format(n, 'o'), '   ', format(n, 'x'))

    # to int from str
    print(int('9C', 16))
    print(int('10011100', 2))

if __name__ == '__main__':
    #test1(12876834.9888)
    bin_oct_hex()
