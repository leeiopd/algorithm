'''
개구리가 연못 위에서 놀고 있다. 개구리는 N개의 연 잎 들을 이용해서 이리저리 뛰어 놀고 있다.

개구리가 뛰는 장면을 보던 철수는 개구리가 도약을 하는 경우가 얼마나 있는지 궁금해졌다. 여기서 도약은 아래 조건을 만족하는 경우를 말한다.

1. 개구리가 뛴 거리가 이전에 뛴 거리 이상 뛰지만 그 2배보다 멀리 뛰지는 않는다.
2. 개구리는 오른쪽으로만 뛴다.
3. 개구리는 두 번만 뛴다.
4. 위 세 가지 조건을 만족한다면 어느 곳에서든 시작할 수 있다.

허나, 연 잎 들이 너무 많기 때문에 가능한 횟수가 매우 많아질 것 같다고 생각한 철수는, 개구리가 오른쪽으로 도약하는 경우가 얼마나 되는지 구해달라고 했다. 철수를 위해 프로그램을 짜주자.

첫 번째 줄에는 연 잎의 수 N(3 ≤ N ≤ 1,000)이 주어진다.
두 번째 줄부터 N개의 줄에는 각 연 잎의 좌표가 주어진다. 모든 좌표는 0 이상 108 이하이다.

 개구리가 오른쪽으로 도약하는 경우의 수를 출력한다.
'''
import sys

sys.stdin = open("C9_input.txt")

N = int(input())

maps = []
for n in range(N):
    maps.append(int(input()))

maps.sort()
cnt = 0
result = [0, 0, 0]
top = -1
for i in maps:
    mem = [0, 0, 0]
    top += 1
    mem[top] = i
    for j in maps:
        if j in mem or j < mem[top]:
            continue
        long = j - mem[top]
        top += 1
        mem[top] = j
        for k in maps:
            if k in mem or k < mem[top]:
                continue
            if long > k - mem[top] or long * 2 < k - mem[top]:
                continue
            top += 1
            mem[top] = k
            cnt += 1
            mem[top] = 0
            top -= 1
        mem[top] = 0
        top -= 1
    mem[top] = 0
    top -= 1
print(cnt)


