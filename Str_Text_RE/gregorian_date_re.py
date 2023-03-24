import re


def test_gd():
    import re

    regex = r"^(0[1-9]|[1-2][0-9]|3[01])[-\./](0[13578]|[1][02])[-\./](\d{3}[1-9])\b$" \
            r"|(0[1-9][1-2][0-9]|30)[-\./](11|0[469])[-\./](\d{3}[1-9])\b$" \
            r"|(0[1-9]|1[0-9]|2[0-8])[-\./](02)[-\./](\d{3}[1-9])\b$" \
            r"|(29)[-\./](02)[-\./]" \
            r"(?=\d{4}$)(?!0+$)\d*(?:(?:[02468][048]|[13579][26])00|(?!00$)(?:[02468][048]|[13579][26]))\b$"

    test_str = ("30.11.1964\n"
                "31.08.2024\n"
                "29.02.1963\n"
                "28/02/2000\n"
                "29-02-1964\n")

    matches = re.finditer(regex, test_str, re.MULTILINE)

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

    print(len(regex))
def greg_date(s: str) -> bool:
    regex = r"^(0[1-9]|[1-2][0-9]|3[01])[-\./](0[13578]|[1][02])[-\./](\d{3}[1-9])\b$" \
            r"|(0[1-9][1-2][0-9]|30)[-\./](11|0[469])[-\./](\d{3}[1-9])\b$" \
            r"|(0[1-9]|1[0-9]|2[0-8])[-\./](02)[-\./](\d{3}[1-9])\b$" \
            r"|(29)[-\./](02)[-\./]" \
            r"(?=\d{4}$)(?!0+$)\d*(?:(?:[02468][048]|[13579][26])00|(?!00$)(?:[02468][048]|[13579][26]))\b$"
    if re.search(regex, s):
        return True
    else:
        return False


if __name__ == '__main__':
    #test_gd()
    print(greg_date("29.02.1964"))
