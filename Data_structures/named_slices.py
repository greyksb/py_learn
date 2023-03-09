# срезы можно именовать
# например  a = slice(2, 10, 2), lst[2: 10: 2] == lst(a)
# объект slice имеет поля a.start a.stop a.step
some_string = "Book's name: Black swan price:   $15.12 pages: 340"
NAME = slice(13,23)
print(some_string[NAME])
print(NAME.start)
print(NAME.stop)
print(NAME.step)
# or
i_start = some_string.find('$')
PRICE = slice(i_start + 1, i_start + 6)
print(float(some_string[PRICE]))

# чтобы не выйти за границы можно использовать indices(size)
a = slice(-3, 126)
print(f'a.start = {a.start} a.stop = {a.stop}')
print(f'a.indices = {a.indices(len(some_string))}')

tp_i = a.indices(len(some_string))
PAGES = slice(tp_i[0], tp_i[1])
print(some_string[PAGES])
