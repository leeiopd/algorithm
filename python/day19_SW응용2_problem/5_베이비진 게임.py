'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys

sys.stdin = open("5_input.txt")

T = int(input())

def check(A):
    if A[0] == A[1] and A[1] == A[2]:
        return 1

    if A[0] + 1 == A[1] and A[1] + 1 == A[2]:
        return 1

    return 0

def game_A(N, k=0):
    global flag_A

    if check(A):
        flag_A = 1
        return 1

    for i in range(k, N):
        A[i], A[k] = A[k], A[i]
        game_A(N, k+1)
        A[i], A[k] = A[k], A[i]

def game_B(N, k=0):
    global flag_B

    if check(B):
        flag_B=1
        return 1

    for i in range(k, N):
        B[i], B[k] = B[k], B[i]
        game_B(N, k+1)
        B[i], B[k] = B[k], B[i]


for case in range(1, T+1):
    cards = list(map(int, input().split()))
    A = []
    B = []
    result = '0'
    point_A = 0
    point_B = 0
    flag_A = 0
    flag_B = 0
    for i in range(6):
        A.append(cards[i*2])
        B.append(cards[i*2+1])

        if i >= 2:
            game_A(len(A))
            game_B(len(B))
            if flag_A:
                point_A = 1
            if point_A > point_B:
                result = '1'
                break
            if flag_B:
                point_B = 1
            if point_B > point_A:
                result = '2'
                break

    print("#{} {}".format(case, result))