import sys
sys.stdin = open("미사일.txt")
'''
 군함에 미사일을 쏴서 군함을 가장 많이 침몰시켜 남은 군함개수를 구한다.
[조건]
1] 미사일의 화력이 미치는 범위 이내에 있는 군함은 동시에 침몰이 가능하다.
2] 군함은 미사일의 화력 만큼 에너지가 없어지며 군함의 에너지가 0이하가 되어야 침몰이 가능하다.
3] 군함이 없는 바다에 발사된 미사일은 폭발범위 이내의 군함에 영향을 주지 못한다. 
4] 미사일은 한 번에 하나씩만 발사된다. 
5] 미사일과 배의 폭발범위 계산식은 D = | x-x1 | + |y-y1| 이다.
     D가 미사일의 화력이 미치는 범위보다 작거나 같을 경우 영항을 미친다. 
    (x, y는 미사일이 떨어진 위치이며 x1, y1은 미사일 주위의 배 위치)

예를 들어 미사일이 떨어진 위치 (x,y)가 (100, 200)이고 미사일 주위의 배 위치 (x1, y1)가 (100,100)인 경우, 
    계신식은 D = |100-100| + |200-100| 로 D의 결과값은 100이다. 
    미사일의 화력이 미치는 범위가 100이하인 경우 영향을 받게 되어 에너지를 차감하게 된다.

Map 크기 1~1000 이며 미사일개수는 1~4개, 군함개수는 1~16개이다. 군함의 에너지는 10 ~ 100사이이다.
미사일의 화력 범위는 10 ~ 500사이이다. 

[입력] 
 3 // 군함수
100 100 40 // 군함의 좌표(x, y), 에너지
100 200 80
300 500 40
2 40 100 //미사일 개수, 화력, 화력이 미치는 범위

'''

N = int(input())
boat = []
for n in range(N):
    boat.append(list(map(int, input().split())))

bomb, fire, wide = map(int, input().split())
set_list = [0] * bomb
result = 0

def shoot(k):
    global boat
    x = boat[k][0]
    y = boat[k][1]
    boat[k][2] -= fire

    for i in range(N):
        if i != k:
            if abs(x - boat[i][0]) + abs(y - boat[i][1]) <= wide:
                boat[i][2] -= fire

def repair(k):
    global boat
    x = boat[k][0]
    y = boat[k][1]
    boat[k][2] += fire

    for i in range(N):
        if i != k:
            if abs(x - boat[i][0]) + abs(y - boat[i][1]) <= wide:
                boat[i][2] += fire

def game(k=0):
    global result
    if k == bomb:
        add = 0
        for i in range(N):
            if boat[i][2] <= 0:
                add += 1
        if add > result:
            result = add
        return

    else:

        for i in range(N):
            if boat[i][2] > 0:
                set_list[k] = i
                shoot(i)
                game(k+1)
                repair(i)

        set_list[k] = 0
        game(k+1)

game()
print(N-result)
