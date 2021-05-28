string = input()

stringList = []
for i in range(len(string)):
    stringList.append(string[i:])

for s in sorted(stringList):
    print(s)
