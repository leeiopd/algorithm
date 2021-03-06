'''
Samsung Collegiate Programming Cup은 Samsung이 매년마다 개최하는 대학생 프로그래밍 축제다.

이 축제의 우승자는 Samsung에 입사할 수 있지만, 나머지 사람들은 시공의 폭풍 속으로 빠지게 된다.

이 축제에서 참가자들은 자신이 선호하는 언어로 프로그램을 작성할 수 있다.

혁진이는 자신이 개발한 언어 혁셈블리어를 이용해 대회에 참가했다.

축제에서 꼭 우승하고 싶은 혁진이는 자신이 작성한 프로그램이 결국에는 멈출 수 있는지 확인하고 싶다.

혁셈블리어는 다음과 같이 동작한다:

    - 프로그램이 수행해야 하는 명령은 문자로 주어지며, 문자들은 2차원 격자 모양으로 줄지어 있다. 다음은 혁셈블리어 프로그램의 예이다.
        6>--v.
        .^--_@

 - 프로그램은 현재 위치에 있는 문자가 나타내는 명령을 처리하고, 이동 방향에 따라 다음 문자로 이동해야 한다.

      가장 처음 위치는 제일 왼쪽 위에 있는 문자이고, 이동 방향은 오른쪽이다.

- 명령을 처리하다 보면 이동 방향이 상하좌우로 바뀔 수 있다.

     만약 다음 이동이 2차원 격자의 바깥으로 이동하는 방향이면, 반대편에 있는 위치로 이동한다.

     예를 들어, 첫 번째 줄의 가장 오른쪽 칸에서 오른쪽 방향으로 이동하면 첫 번째 줄의 가장 왼쪽 칸으로 이동한다.

     혁셈블리어에서는 메모리가 단 하나 있으며, 0에서 15사이의 정수를 하나 저장할 수 있다. 가장 처음에는 0이 저장되어 있다.

사용 가능한 명령은 아래와 같다:


문자	수행 명령
<	이동 방향을 왼쪽으로 바꾼다.
>	이동 방향을 오른쪽으로 바꾼다.
^	이동 방향을 위쪽으로 바꾼다.
v	이동 방향을 아래쪽으로 바꾼다.
_	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
|	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
.	아무 것도 하지 않는다.
@	프로그램의 실행을 정지한다.
0~9	메모리에 문자가 나타내는 값을 저장한다.
+	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
-	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 R, C (2 ≤ R, C ≤ 20) 가 공백으로 구분되어 주어진다.

이는 프로그램이 R행 C열의 문자로 이루어짐을 나타낸다.

다음 R개의 줄의 각 줄에는 C개의 문자로 이루어진 문자열이 주어진다. 주어지는 문자는 위에서 주어진 문자들이다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

주어진 프로그램이 정지할 수 있으면 “YES”를 출력하고, 아니면 “NO”를 출력한다.
'''
import sys
sys.stdin = open('1824.txt')

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for case in range(1, T+1):
    R, C = map(int, input().split())
    maps = []
    for r in range(R):
        maps.append(input())
    flag = 0
    for y in range(R):
        if '@' in maps[y]:
            flag = 1

    if not flag:
        print('#{} NO'.format(case))
    else:
        tmp = [[0, 0, 0, 0]]
        check = [[[0, 0, 0, 0] for c in range(C)] for r in range(R)]
        result = 'NO'
        while tmp:
            if len(tmp) >= 1000:
                break
            x, y, memory, arrow = map(int, tmp.pop())
            check[y][x][arrow] += 1

            if maps[y][x] == '<':
                arrow = 1
                X = x + dx[arrow]
                X %= C
                if check[y][X][arrow] <= 20:
                    tmp.append([X, y, memory, arrow])
            elif maps[y][x] == '>':
                arrow = 0
                X = x + dx[arrow]
                X %= C
                if check[y][X][arrow] <= 20:
                    tmp.append([X, y, memory, arrow])
            elif maps[y][x] == '^':
                arrow = 2
                Y = y + dy[arrow]
                Y %= R
                if check[Y][x][arrow] <= 20:
                    tmp.append([x, Y, memory, arrow])
            elif maps[y][x] == 'v':
                arrow = 3
                Y = y + dy[arrow]
                Y %= R
                if check[Y][x][arrow] <= 20:
                    tmp.append([x, Y, memory, arrow])
            elif maps[y][x] == '_':
                if memory == 0:
                    arrow = 0
                else:
                    arrow = 1
                X = x + dx[arrow]
                X %= C
                if check[y][X][arrow] <= 20:
                    tmp.append([X, y, memory, arrow])
            elif maps[y][x] == '|':
                if memory == 0:
                    arrow = 3
                else:
                    arrow = 2
                Y = y + dy[arrow]
                Y %= R
                if check[Y][x][arrow] <= 20:
                    tmp.append([x, Y, memory, arrow])
            elif maps[y][x] == '?':
                for i in range(4):
                    X = x + dx[i]
                    Y = y + dy[i]
                    X %= C
                    Y %= R
                    if check[Y][X][arrow] <= 20:
                        tmp.append([X, Y, memory, i])
            elif maps[y][x] == '.':
                X = x + dx[arrow]
                Y = y + dy[arrow]
                X %= C
                Y %= R
                if check[Y][X][arrow] <= 20:
                    tmp.append([X, Y, memory, arrow])
            elif maps[y][x] == '@':
                result = 'YES'
                break
            elif maps[y][x] == '+':
                if memory == 15:
                    memory = 0
                else:
                    memory += 1
                X = x + dx[arrow]
                Y = y + dy[arrow]
                X %= C
                Y %= R
                if check[Y][X][arrow] <= 20:
                    tmp.append([X, Y, memory, arrow])
            elif maps[y][x] == '-':
                if memory == 0:
                    memory = 15
                else:
                    memory -= 1
                X = x + dx[arrow]
                Y = y + dy[arrow]
                X %= C
                Y %= R
                if check[Y][X][arrow] <= 20:
                    tmp.append([X, Y, memory, arrow])
            else:
                memory = int(maps[y][x])
                X = x + dx[arrow]
                Y = y + dy[arrow]
                X %= C
                Y %= R
                if check[Y][X][arrow] <= 20:
                    tmp.append([X, Y, memory, arrow])
        print('#{} {}'.format(case, result))
