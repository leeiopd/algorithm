import sys
sys.stdin = open("Nqueen.txt")
'''
체스에서 queen의 가로, 세로, 대각선 방향으로 어느 곳이나 한 번에 움직일 수 있다.
즉 다음과 같은 체스판에서 queen이 X라고 표시된 위치에서 있을 때, 그 다음 queen이 움직여 갈 수 있는 부분은 어둡게 칠해진 부분 중의 하나이다.

N*N 크기의 정방형 체스판이 주어졌다.
우리는 거기에 N개의 queen을 배치하려고 하는데, 모든 queen들은 서로 잡아먹을 수 없어야 한다.
그렇다면 queen들을 어떻게 배치해야만 할까? 가능한 모든 경우의 개수를 출력한다.

Queen의 수 N(1≤N≤10)을 입력 받는다.
N*N의 체스판에서 N개의 queen들이 서로 잡아먹지 않는 위치로 놓을 수 있는 방법의 수를 출력한다.
'''

N = int(input())

def Nqueen(k=0):
    global result

    if k == N:
        result += 1
        return

    for x in range(N):
        if check_x[x] == 1:
            continue
        if check_rightDown[x+k] == 1:
            continue
        if check_leftDown[(N-1)-(k-x)] == 1:
            continue

        check_x[x] = 1
        check_rightDown[x + k] = 1
        check_leftDown[(N - 1) - (k - x)] = 1
        Nqueen(k+1)
        check_x[x] = 0
        check_rightDown[x + k] = 0
        check_leftDown[(N - 1) - (k - x)] = 0

check_x = [0] * 10
check_rightDown = [0] * 1000
check_leftDown = [0] * 10000
result = 0
Nqueen()
print(result)