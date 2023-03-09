from itertools import groupby
from operator import itemgetter
from itertools import compress

# приемы группирования и фильтрации списков

def group_by_field():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    # сначала сортируем этот список по полю date
    rows.sort(key=itemgetter('date'))
    # группируем
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for item in items:
            print('\t', item)


# фильтрация одной последовательности на основании другой последовательности, связанной с этой
# с использованием compress

# например, есть список студентов и список их оценок по крайнему экзамену
# необходимо сформировать список на пересдачу (т.е. тех, кто получил ниже 5 из 12)

def make_non_graduate_lst():
    students = [
        'Vovk',
        'Scheptun',
        'Kalinicheko',
        'Lukiyanova'
    ]
    grades = [5, 4, 12, 11]
    print(list(compress(students,[True if x < 5 else False for x in grades])))


if __name__ == '__main__':
    # testing group_by_field()
    # group_by_field()

    # testing make_non_graduate_lst()
    make_non_graduate_lst()
