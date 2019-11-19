import sys

sys.stdin = open("03_input.txt")

T = int(input())

for case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [[0, 0, 0, 0] for x in range(N+1)]
    parents = 0
    cnt = 0
    for n in range(1, len(nums)+1):
        cnt += 1
        tree[n][2] = nums[n-1]
        tree[n][0] = n*2
        tree[n][1] = n*2 + 1
        tree[n][3] = n//2
        k = n
        while tree[k][3] != 0:
            if tree[k][2] < tree[tree[k][3]][2]:
                tree[k][2], tree[tree[k][3]][2] = tree[tree[k][3]][2], tree[k][2]
            k = tree[k][3]

    result = 0
    root = tree[N][3]
    while True:
        result += tree[root][2]
        if root==1:
            break


        root = tree[root][3]

    print(f'#{case} {result}')