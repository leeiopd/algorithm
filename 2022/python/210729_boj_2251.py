from collections import deque

A, B, C = map(int, input().split())

water = C

queue = deque()
queue.append([0, 0, C])
res = set()
visited = set()


# 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
# (용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램
# 8 9 10 -> 1 2 8 9 10
while queue:
    a, b, c = queue.popleft()

    if (a, b, c) in visited:
        continue
    else:
        visited.add((a, b, c))

    if not a:
        res.add(c)

    if a+b > B:
        queue.append([a+b-B, B, c])
    else:
        queue.append([0, a+b, c])

    if a+c > C:
        queue.append([a+c-C, b, C])
    else:
        queue.append([0, b, a+c])

    if b+c > C:
        queue.append([a, b+c-C, C])
    else:
        queue.append([a, 0, b+c])

    if b+a > A:
        queue.append([A, b+a-A, c])
    else:
        queue.append([b+a, 0, c])

    if c+a > A:
        queue.append([A, b, c+a-A])
    else:
        queue.append([c+a, b, 0])

    if c+b > B:
        queue.append([a, B, c+b-B])
    else:
        queue.append([a, c+b, 0])

res = list(res)
res.sort()
print(" ".join(map(str, res)))
