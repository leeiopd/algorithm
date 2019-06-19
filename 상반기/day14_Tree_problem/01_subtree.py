import sys

sys.stdin = open("01_input.txt")

T = int(input())

def check(N):
    global cnt
    if N != 0:
        cnt += 1
        check(tree[N][0])
        check(tree[N][1])


for case in range(1, T+1):
    E, N = map(int, input().split())
    long = list(map(int, input().split()))
    tree = [[0, 0] for x in range(1002)]
    for i in range(E):
        root = long[2 * i]
        son = long[(2*i) +1]
        if tree[root][0] == 0:
            tree[root][0] = son
        else:
            tree[root][1] = son
    cnt = 0
    check(N)
    print(f'#{case} {cnt}')