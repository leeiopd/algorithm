import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    nums = list(map(int, input().split()))
    nums = [0] + nums

    cnt = 0

    for f in range(1, N+1):
        if nums[f] < 0:
            continue
        cnt += 1
        t = nums[f]
        nums[f] = -1
        while True:
            if t < 0:
                break
            f = t
            t = nums[f]
            nums[f] = -1
    print(cnt)
