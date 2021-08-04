from collections import deque

F, S, G, U, D = map(int, input().split())

# 가장 높은 층은 F층이다.
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
# U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다.
# (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

queue = deque()
queue.append((S, 0))

visited = [0] * (F+1)
visited[S] = 1
res = F
while queue:
    s, cnt = queue.popleft()

    # 경우의 수가 더 많아진다.
    # visited[s] = 1
    if s == G:
        res = min(res, cnt)
        break

    if s + U <= F and not visited[s+U]:
        visited[s+U] = 1
        queue.append((s+U, cnt+1))

    if s - D >= 1 and not visited[s-D]:
        visited[s-D] = 1
        queue.append((s-D, cnt+1))


if res == F:
    print("use the stairs")
else:
    print(res)
