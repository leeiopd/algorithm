'''
정사각형의 크기를 입력 받은 후, 시계방향으로 돌면서 다음과 같은 형태로 출력하는 프로그램을 작성하시오.
 
< 처리조건 >
(1) 가장 왼쪽 위의 좌표부터 차례로 숫자를 대입시킨다.
(2) 오른쪽으로 채워 나가다가 끝이면 다시 아래 -> 왼쪽 -> 위 -> 오른쪽의 순으로 모두 채워질 때까지 반복한다. 


정사각형의 크기 n(1부터 100사이의 정수)을 입력 받는다.

위에서 언급한 형태로 정사각형의 내부 숫자를 차례로 채운 후의 모습을 출력한다. 숫자 사이는 공백으로 구분한다.
'''
import sys

sys.stdin = open("A9_input.txt")

N = int(input())

maps = [ [ 0 for x in range(N)] for y in range(N) ]


def check(i):
    X = x + dx[i]
    Y = y + dy[i]
    
    if i == 0:
        if X < N and maps[Y][X] == 0:
            return 0
        else:
            return 2
            
    elif i == 1:
        if X > -1 and maps[Y][X] == 0:
            return 1
        else:
            return 3
            
    elif i == 2:
        if Y < N and maps[Y][X] == 0:
            return 2
        else:
            return 1
    elif i == 3:
        if Y > -1 and maps[Y][X] == 0:
            return 3
        else:
            return 0

    

cnt = 0
i = 0
x = 0
y = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while cnt < N*N:
    cnt += 1
    maps[y][x] = cnt
    i = check(i)
    x = x + dx[i]
    y = y + dy[i]
    

for y in range(N):
    result = ' '.join(map(str, maps[y]))
    print(result)