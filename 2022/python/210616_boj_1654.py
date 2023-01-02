import sys
input = sys.stdin.readline


K, N = map(int, input().split())

lines = []

for _ in range(K):
    lines.append(int(input()))

end = max(lines)
start = 1

while start <= end:
    mid = (start+end) // 2
    res = 0

    for l in lines:
        res += l // mid

    if res < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)
