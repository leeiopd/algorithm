import sys

sys.stdin = open("7_input.txt")

'''
승훈이는 심심한 시간에 스타크래프트(Starcraft) 게임을 하며 놀고 있었다.
스타크래프트유닛중 하나인 저글링을 한 곳에 몰아세운 뒤, 방사능 오염 공격으로 없애보려고 했다.
그런데 좀 더 재미있게 게임을 하기 위해서 게임을 개조하여 방사능 오면 공격을 가하면 방사능은 1초마다 이웃한 저글링에 오염된다.
그리고 방사능에 오염된 저글링은 3초 후에 죽게 된다.
예를 들어 아래 왼쪽그림과 같이 모여 있는 저글링 중에 빨간 동그라미 표시를 한 저글링에게 방사능 오염공격을 가하면, 총 9초 후에 저글링들이 죽게 된다.
아래 오른쪽에 있는 그림의 숫자들은 각 저글링들이 죽는 시간이다.
 
첫째 줄은 지도의 가로 세로 크기가 주어진다. 지도는 격자 구조로 이루어져 있으며 크기는 100×100칸을 넘지 않는다.
둘째 줄부터는 지도상에 저글링들이 놓여있는 상황이 주어진다. 1은 저글링이 있는 곳의 표시이고 0은 없는 곳이다.
마지막 줄에는 방사능오염을 가하는 위치가 가로 세로 위치로 주어진다.
 '''

X, Y = map(int, input().split())

maps = [[0 for x in range(X+2)]]

for y in range(Y):
    y_line = [0] + list(map(int, input())) + [0]
    maps.append(y_line)

maps.append([0 for x in range(X+2)])

start_x, start_y = map(int, input().split())

cnt  = 1
queue = [[start_x, start_y, cnt]]
maps[start_y][start_x] = 3
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


while queue:
    x, y, cnt = queue.pop(0)
    cnt += 1


    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if maps[next_y][next_x] == 1:
            maps[next_y][next_x] = 3
            queue.append([next_x, next_y, cnt])
check = 0
for y in range(Y+2):
    for x in range(X+2):
        if maps[y][x] == 1:
            check += 1

print(cnt)
print(check)