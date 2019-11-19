import sys
sys.stdin = open("파이프제거.txt")

'''
도시의 지하에는 수많은 수도파이프가 설치 되어있다. 하지만 이 수도 파이프들이 너무나 무계획적으로 설치되었기 때문에,
실제로는 물이 흐르지 않는 수도파이프도 다수 설치되어 있다고 한다. 
그래서 수도파이프 배치를 설계하는 사람들이 현재 도시의 수도파이프 설치 상태를 확인한 뒤, 실제 물이 흐르지 않는 수도파이프를 제거하는 공사를 시행하려 한다.
 
다음과 같이 파이프가 설치된 상태에서 (0,0) 수도 공급원 이라고 한다면 5개의 수도파이프는 물이 흐르지 않는 수도 파이프이므로 제거 대상이 된다.
 
다음과 같이 도시의 지하 수도파이프 설치 지도와 수도공급원의 위치가 주어졌을 때, 제거해야 할 수도 파이프의 개수를 구하시오.

입력의 첫째 줄에는 정사각형의 지도의 가로 사이즈 N이 주어진다. ( 4 <= N <= 10)
둘째 줄에는 수도공급원의 시작 좌표가 X,Y의 순서로 주어진다. ( 0<=X,Y<= 9 )
셋째 줄부터 N개의 줄에는 N X N 사이즈의 지도에 대한 정보가 주어진다.
지도 한칸의 파이프에 대한 정보는 숫자 0~9 그리고 A, B로 표현되며 그 의미는 다음과 같다.
0-(파이프 없음)
1 – (─), 2-(│), 3- (┌), 4 – (┐), 5-(┘),
6-(└), 7-(├), 8-(┬), 9-(┤), A-(┴), B-(┼)

사용되지 않은 파이프의 수를 출력한다.
'''
N = int(input())
start_x, start_y = map(int, input().split())

maps = []
for n in range(N):
    maps.append(list(map(str, input())))

total = 0



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(x, y, pipe):
    global dx, dy
    maps[y][x] = '0'
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        '''
        1 – (─), 2-(│), 3- (┌), 4 – (┐), 5-(┘),
        6-(└), 7-(├), 8-(┬), 9-(┤), A-(┴), B-(┼)
        '''

        if X > -1 and X < N and Y > -1 and Y < N and maps[Y][X] != '0':
            if i == 0:
                if pipe == '1' or pipe == '3' or pipe == '6' or pipe == '7' or pipe == '8' or pipe == 'A' or pipe == 'B':
                    if maps[Y][X] == '1' or maps[Y][X] == '4' or maps[Y][X] == '5' or maps[Y][X] == '8' or maps[Y][X] == '9' or maps[Y][X] == 'A' or maps[Y][X] == 'B':

                        check(X, Y, maps[Y][X])
            elif i == 1:
                if pipe == '1' or pipe == '4' or pipe == '5' or pipe == '8' or pipe == '9' or pipe == 'A' or pipe == 'B':
                    if maps[Y][X] == '1' or maps[Y][X] == '3' or maps[Y][X] == '6' or maps[Y][X] == '7' or maps[Y][X] == '8' or maps[Y][X] == 'A' or maps[Y][X] == 'B':

                        check(X, Y, maps[Y][X])
            elif i == 2:
                if pipe == '2' or pipe == '3' or pipe == '4' or pipe == '7' or pipe == '8' or pipe == '9' or pipe == 'B':
                    if maps[Y][X] == '2' or maps[Y][X] == '5' or maps[Y][X] == '6' or maps[Y][X] == '7' or maps[Y][X] == '9' or maps[Y][X] == 'A' or maps[Y][X] == 'B':

                        check(X, Y, maps[Y][X])
            else:
                if pipe == '2' or pipe == '5' or pipe == '6' or pipe == '7' or pipe == '9' or pipe == 'A' or pipe == 'B':
                    if maps[Y][X] == '2' or maps[Y][X] == '3' or maps[Y][X] == '4' or maps[Y][X] == '7' or maps[Y][X] == '8' or maps[Y][X] == '9' or maps[Y][X] == 'B':

                        check(X, Y, maps[Y][X])

check(start_x, start_y, maps[start_y][start_x])
for y in range(N):
    for x in range(N):
        if maps[y][x] != '0':
            total += 1
print(total)