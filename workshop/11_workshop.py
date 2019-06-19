import sys

sys.stdin = open("11_input.txt")

T = 10

for case in range(1, T+1):
    long, start = map(int, input().split())

    from_to = list(map(int, input().split()))
    call_list = []

    for i in range(len(from_to)//2):
        k = [from_to[i*2]]
        k.append(from_to[(i*2) + 1])
        call_list.append(k)
    maps = [[ 0 for x in range(101)] for y in range(101)]

    for call in call_list:
        x = call[1]
        y = call[0]
        maps[y][x] = 1

    visited = [0 for x in range(101)]

    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        k = queue.pop(0)


        for call in range(1, 101):
            if maps[k][call] == 1:
                if visited[call] == 0:
                    visited[call] = visited[k] + 1
                    queue.append(call)
    result = 0
    for i in range(1, 101):
        if visited[i] == max(visited):
            mem = i
            if mem > result:
                result = mem
    print(result)
