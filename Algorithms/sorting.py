# сортировка с использованием itemgetter from operator
from operator import itemgetter

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
{'fname': 'Alan', 'lname': 'Jones', 'uid': 1005}
]
print(*[f"{row['fname']} {row['lname']}" for row in rows], sep='\n')
print()
print(*[f"{row['fname']} {row['lname']}" for row in sorted(rows, key=itemgetter('lname'))], sep='\n')
print()
print(*[f"{row['fname']} {row['lname']}" for row in sorted(rows, key=itemgetter('lname', 'fname'))], sep='\n')
print()

tp = ((1, 2), (34, 8), (2, 17), (16, 1))
print(sorted(tp, key=itemgetter(1)))
print(sorted(tp, key=itemgetter(0, 1)))


# сортировка с lambda key без itemgetter (работает медленнее)
print()
print(*[f"{row['fname']} {row['lname']}" for row in sorted(rows, key=lambda r: (r['lname'], r['fname']))], sep='\n')
print()

#tp = ((1, 2), (34, 8), (2, 17), (16, 1))
print(tp)
print(sorted(tp, key=lambda x: x[1]))
print(sorted(tp, key=lambda x: x[0]))
