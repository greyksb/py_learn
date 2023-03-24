import re


def simple_1():
    """ Найти все слова в тексте, если известно, что в слове могут быть только буквы или знак минус (дефис)
    """

    regex = r"[\b\w+[-]{0,}\w+\b]{0,}"

    test_str = ("Он --- серо-буро-малиновая редиска!! \n"
                ">>>:-> \n"
                "А не кот. \n"
                "www.kot.ru")

    test_str = "Он --- серо-буро-малиновая редиска!! \n>>>:-> \nА не кот. \nwww.kot.ru\n"

    matches = re.finditer(regex, test_str)

    for matchNum, match in enumerate(matches, start=1):

        print("Соответствие {matchNum} было найдено в {start}-{end}: {match}".format(matchNum=matchNum,
                                                                                     start=match.start(),
                                                                                     end=match.end(),
                                                                                     match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Группа {groupNum} найдена в {start}-{end}: {group}".format(groupNum=groupNum,
                                                                              start=match.start(groupNum),
                                                                              end=match.end(groupNum),
                                                                              group=match.group(groupNum)))
    print()
    #находим только первое совпадение шаблона в текста
    matches = re.search(regex, test_str)

    if matches:
        print("Соответствие найдено в {start}-{end}: {match}".format(start=matches.start(), end=matches.end(),
                                                                     match=matches.group()))

        for groupNum in range(0, len(matches.groups())):
            groupNum = groupNum + 1

            print("Группа {groupNum} найдена в {start}-{end}: {group}".format(groupNum=groupNum,
                                                                              start=matches.start(groupNum),
                                                                              end=matches.end(groupNum),
                                                                              group=matches.group(groupNum)))


def simple_2():
    """     поиск с ранее совпавшим текстом
     например, надо найти магические даты в тексте...  т.е. такие, у которых день месяц и год - одно число"""
    # coding=utf8
    # the above tag defines encoding for this document and is for Python 2.x compatibility

    import re

    regex = r"\d\d(\d\d)[./-]\1[./-]\1"

    test_str = ("2012.12.12\n"
                "2023.08.08\n"
                "2001.01.01\n")
    print(test_str)

    matches = re.finditer(regex, test_str)

    for matchNum, match in enumerate(matches, start=1):

        print("Соответствие {matchNum} было найдено в {start}-{end}: {match}".format(matchNum=matchNum,
                                                                                     start=match.start(),
                                                                                     end=match.end(),
                                                                                     match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Группа {groupNum} найдена в {start}-{end}: {group}".format(groupNum=groupNum,
                                                                              start=match.start(groupNum),
                                                                              end=match.end(groupNum),
                                                                              group=match.group(groupNum)))


def simple_3():
    """ именованое сохранение и именованные обратные сслылки"""
    # coding=utf8
    # the above tag defines encoding for this document and is for Python 2.x compatibility

    import re

    regex = r"\b\d\d(?P<year>\d\d)[./-](?P<month>\d\d)[./-](?P=year)"

    test_str = ("2012.12.12\n"
                "2023.08.08\n"
                "2001.01.01\n")

    matches = re.finditer(regex, test_str)

    for matchNum, match in enumerate(matches, start=1):

        print("Соответствие {matchNum} было найдено в {start}-{end}: {match}".format(matchNum=matchNum,
                                                                                     start=match.start(),
                                                                                     end=match.end(),
                                                                                     match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Группа {groupNum} найдена в {start}-{end}: {group}".format(groupNum=groupNum,
                                                                              start=match.start(groupNum),
                                                                              end=match.end(groupNum),
                                                                              group=match.group(groupNum)))

    # Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.


if __name__ == '__main__':
    print(simple_3.__doc__)
    simple_3()
