import sys

sys.stdin = open("0_input.txt")

N = int(input())

arr = list(map(int, input().split()))


def Qsort(s, e):  # s = start, e = end
    if s >= e: return
    pivot = e
    target = s
    for left in range(s, e + 1):
        if arr[left] < arr[pivot]:  # 비교는 left <-> pivot
            # if left != target: left랑 target이 같은 위치면 굳이 바꿀 필요가 없으므로 넣어주는 조건문, 하지만 시간적으로 크게 차이가 나진 않는다.
            arr[left], arr[target] = arr[target], arr[left]  # 비교는 left <-> target
            target += 1
    # if target != pivot: 마찬가지의 경우, 시간 차이가 크게 안난다.
    arr[target], arr[pivot] = arr[pivot], arr[target]
    Qsort(s, target - 1)
    Qsort(target + 1, e)


Qsort(0, N - 1)

for n in arr:
    print(n, end=" ")