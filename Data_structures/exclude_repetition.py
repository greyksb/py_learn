# если необходимо убрать из списка повторяющиеся элементы с сохранением порядка
# set() порядок не сохраняет

# вариант если элементы списка хешируемые:

def dedupe_simple(items: list):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# test dedupe() : [1, 2, 3, 4, 3, 4, 5] for expected [1, 2, 3, 4, 5]
# lst = [1, 2, 3, 4, 3, 4, 5]
# print(list(dedupe_simple(lst)))

# для случая когда список состоит не из хешируемых элементов,
# например, словарей необходима функция преобразования элемента к хешируемым

def dedupe(items: list, key=None) -> iter:
    seen = set()
    for item in items:
        val = item if key == None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# test dedupe2() : [1, 2, 3, 4, 3, 4, 5] for expected [1, 2, 3, 4, 5]
lst = [1, 2, 3, 4, 3, 4, 5]

print(list(dedupe(lst)))

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(list(dedupe(a, lambda d: d['x'])))

print(list(dedupe(a, lambda d: d['y'])))

print(list(dedupe(a, lambda d: (d['x'], d['y']))))
