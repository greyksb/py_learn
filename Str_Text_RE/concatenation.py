# если возникает необходимость сцепления строк, то всегда актуален вопрос производительности
# + - не всегда лучшее решение
# здесь представлены варианты подходов
#

def gen_strs():
    """
    если необходимо сцепить несколько не очень длинных строк, то имеет смысл сделать это через генератор

    """
    yield 'String1'
    yield 'String2'
    yield 'String3'
    yield 'String4'
    yield 'String5'


def combine(source, maxsize):
    """ можно накапливать отслеживая объем и выдавать порциями maxsize

    """
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
        parts = []
        size = 0
        yield ''.join(parts)


def test_concat():
    print(' '.join(gen_strs()))

if __name__ == '__main__':
    test_concat()
