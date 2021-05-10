import sys

sys.stdin = open("04_input.txt")

T = int(input())

for case in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [[0, 0, 0, 0] for x in range(N+1)]    # [왼쪽 자식, 오른쪽 자식, 부모, data]

    for n in range(1, N+1):
        tree[n][0] = 2*n
        tree[n][1] = 2 * n + 1
        tree[n][2] = n//2

    for m in range(M):
        node, value = map(int, input().split())
        tree[node][3] = value

    for i in range(N, 0, -1):
        tree[tree[i][2]][3] = tree[tree[i][2]][3] + tree[i][3]

    print(f'#{case} {tree[L][3]}')