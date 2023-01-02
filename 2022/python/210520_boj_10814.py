import sys
N = int(sys.stdin.readline())

persons = []

for _ in range(N):
    persons.append(list(map(lambda x: int(x) if x.isdecimal() else x ,sys.stdin.readline().split())))
    

for person in sorted(persons, key = lambda x: x[0]):
    print(person[0], person[1])