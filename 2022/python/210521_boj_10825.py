import sys

N = int(sys.stdin.readline())
studentWithScore = []
for _ in range(N):
    studentWithScore.append(list(map(lambda x: int(x) if x.isdecimal() else x,sys.stdin.readline().split())))
    
for s in sorted(studentWithScore, key = lambda x: (-x[1], x[2], -x[3], x[0])):
    print(s[0])