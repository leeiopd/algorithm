N, M, K = map(int, input().split())

team = N//2

while team > M:
    team -= 1

while N+M-(3*team) < K:
    team -= 1

print(team)
