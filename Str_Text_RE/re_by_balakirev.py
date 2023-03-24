import re


def lesson_1():
    """    пример использования re для построение списка кортежей ключ, значение из строки
    в качестве ключей нужно выбрать только key1 и key2
    для решения используются сохраняющие скобки и группировка
    """
    s = 'key1=value1 a = 345 key2  = 777'
    print(f'Исходная строка: {s}')
    rgx = r"(key1|key2)\s*=\s*(\w+)"
    matches = re.findall(rgx, s)
    print(matches)
    # print(dict(matches))


def lesson_2():
    """
    это задача из CodeWars Regular Expressions (groups): Splitting phone numbers into teir separate parts
    """

    true_numbers = ['+12 34 567890',
                    '034 567890',
                    '567890',
                    '0012 34 567890',
                    '090 500000',
                    '+380673259581',
                    '067 3259581']

    false_numbers = ['0001 34 567890',
                     '+01 34 567890',
                     '+12 04 567890',
                     '+12 034 567890',
                     '+12 34 067895',
                     '034 067895',
                     '001 567890',
                     '098765',
                     '+12 34 5567890',
                     '+12 34 567890 ']
    # rgx = r"(?:\+|00)(?=([1-9]\d) ([1-9]\d) ([1-9]\d{5}$))|(0[1-9]\d)(?= ([1-9]\d{5}$))|(^[1-9]\d{5}$)"
    #    rgx = "(?P<t1>)?(\+|00)(?(t1)([1-9]\d) ([1-9]\d)([1-9]\d{5}$)|(?:(?P<t2>)?(0[1-9]\d)(?(t2)([1-9]\d{5}$)|(^[1-9]\d{5}$))))"
    rgx = r"(?:\+|00)(?=([1-9]\d{1,2})\s*([1-9]\d)\s*([1-9]\d{5,6}$))|(^0[1-9]\d)\s*([1-9]\d{5,6}$)|(^[1-9]\d{5,6}$)"
    print('Testing true numbers:')
    # m = re.finditer(rgx, true_numbers[0])
    # for e in m:
    #     print(e.groups())


    for number in true_numbers:
        matches = re.findall(rgx, number)
        print(matches)

    print()

    print('Testing false numbers:')
    for number in false_numbers:
        matches = re.findall(rgx, number)
        print(matches)


if __name__ == '__main__':
    # print(lesson_1.__doc__)
    lesson_2()
