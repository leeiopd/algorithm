import sys
sys.stdin = open("주사위던지기.txt")
'''
주사위를 던진 횟수 N과 출력형식 M을 입력 받아서 M의 값에 따라 각각 아래와 같이 출력하는 프로그램을 작성하시오.
M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
* 중복의 예
1 1 2 와 중복 : 1 2 1, 2 1 1
1 2 3 과 중복 : 1 3 2, 2 1 3, 2 3 1, 3 1 2

첫 줄에 주사위를 던진 횟수 N(2≤N≤5)과 출력모양 M(1≤M≤3)이 들어온다.

주사위를 던진 횟수 N에 대한 출력모양을 출력한다.
작은 숫자부터 출력한다.
'''
N, M = map(int, input().split())

set_list = [0] * N
visited = []
cnt = 0
def game_1(k=0):
    global cnt
    if k == N:
        cnt += 1
        print(' '.join(map(str, set_list)))

    else:
        for i in range(1, 7):
            set_list[k] = i
            game_1(k+1)
            set_list[k] = 0

def game_2(k=0):
    global cnt
    if k == N:
        mem = [0] * N
        for i in range(N):
            mem[i] = set_list[i]
        mem.sort()
        if mem in visited:
            return
        else:
            cnt += 1
            visited.append(mem)
            print(' '.join(map(str, mem)))

    else:
        for i in range(1, 7):
            set_list[k] = i
            game_2(k+1)
            set_list[k] = 0

def game_3(k=0):
    global cnt

    if k == N:
        cnt += 1
        print(' '.join(map(str, set_list)))

    else:
        for i in range(1, 7):
            if i not in set_list:
                set_list[k] = i
                game_3(k+1)
                set_list[k] = 0

if M == 1:
    game_1()
    print(cnt)

elif M==2:
    game_2()
    print(cnt)

elif M==3:
    game_3()
    print(cnt)