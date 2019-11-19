import sys
sys.stdin = open("04_input.txt")

T = int(input())

def choice(visited, k, add):
    global result
    k += 1
    if k == N:                                 # N 개의 순열이 완성 되면 리턴
        if add < result:
            result = add
        return

    for x in range(N):
        if x not in visited:
            visited[k] = x					   # 방문 기록
            
            if (add + maps[k][x]) < result:	   # 이전 시행의 result 값보다 작아야 동작
                add += maps[k][x]
                choice(visited, k, add)        # 재귀
                add -= maps[k][x]              # 동작후 저장된 k번째 값 clear
                visited[k] = -99               # k 번째 visited 메모리 clear
            
            else:
                visited[k] = -99

for case in range(1, T+1):
    N = int(input())
    maps = []
    visited = [ -99 ] * N
    k = -1
    add = 0
    result = 1000000000
    for n in range(N):
        maps.append(list(map(int, input().split())))
    
    choice(visited, k, add)

    print(f'#{case} {result}')
