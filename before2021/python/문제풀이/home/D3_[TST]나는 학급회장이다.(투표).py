import sys

sys.stdin = open("D3_input.txt")

N = int(input())

people = [[0, 0, 0]]

for n in range(N):
    k = list(map(int, input().split()))
    people.append(k)

score = [[0, 0, x] for x in range(4)]

for p in people:
    score[1][0] += p[0]
    if p[0] == 3:
        score[1][1] += 1

    score[2][0] += p[1]
    if p[1] == 3:
        score[2][1] += 1

    score[3][0] += p[2]
    if p[2] == 3:
        score[3][1] += 1

score.sort(reverse=True)
score.sort(reverse=True)
print(score)

if score[0][0] == score[1][0] and score[0][1] == score[1][1]:
    print(score[0][0])

else:
    print(score[0][2])