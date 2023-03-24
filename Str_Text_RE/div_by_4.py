def div_by_4():
    # coding=utf8
    # the above tag defines encoding for this document and is for Python 2.x compatibility

    import re

    regex = r"(?:[\w\W]*\[[-\+]*0*)(\d+)(?=\])(?<=(?:[13579][26]|[2468][048]))|(?:^\[-*\+*0*)(\d+)(?=\]$)(?<=(?:[48]))"     #|

    test_str = ["[-0]",
                "No [2016] isnt"
                "[+002014]",
                "[+05620]",
                "[+05623]",
                "[-0]",
                "[32]",
                "[5640]",
                "~[4]"]
    for e in test_str:
        m = re.findall(regex, e)
        print(m)



if __name__ == '__main__':
    div_by_4()
