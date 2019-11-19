'''
개구리가 연못 위에서 놀고 있다. 개구리는 N개의 연 잎 들을 이용해서 이리저리 뛰어 놀고 있다.

개구리가 뛰는 장면을 보던 철수는 개구리가 도약을 하는 경우가 얼마나 있는지 궁금해졌다. 여기서 도약은 아래 조건을 만족하는 경우를 말한다.

1. 개구리가 뛴 거리가 이전에 뛴 거리 이상 뛰지만 그 2배보다 멀리 뛰지는 않는다.
2. 개구리는 오른쪽으로만 뛴다.
3. 개구리는 두 번만 뛴다.
4. 위 세 가지 조건을 만족한다면 어느 곳에서든 시작할 수 있다.

허나, 연 잎 들이 너무 많기 때문에 가능한 횟수가 매우 많아질 것 같다고 생각한 철수는, 개구리가 오른쪽으로 도약하는 경우가 얼마나 되는지 구해달라고 했다.

철수를 위해 프로그램을 짜주자.

첫 번째 줄에는 연 잎의 수 N(3 ≤ N ≤ 1,000)이 주어진다.
두 번째 줄부터 N개의 줄에는 각 연 잎의 좌표가 주어진다. 모든 좌표는 0 이상 108 이하이다.
'''

import sys

sys.stdin = open("4_input.txt")

N = int(input())

leaf = [0] * N

def up_leaf(s, e, d):
    m = -1
    sol = -1

    while s <= e:
        m = (s + e) // 2
        if leaf[m] < d:
            s = m + 1
            sol = m +1
        else:
            e = m - 1
    return sol




for n in range(N):
    leaf[n] = int(input())


for i in range(N-1):
    for j in range(i+1, N):
        if leaf[i] > leaf[j]:
            leaf[i], leaf[j] = leaf[j], leaf[i]
result= 0


for i in range(n-1):
    for j in range(i+1, n):
        jump = leaf[j] - leaf[i]
        result += up_leaf(1, n, leaf[j] + 2 * jump + 1) - up_leaf(1, n, leaf[j] + jump)

print(result)