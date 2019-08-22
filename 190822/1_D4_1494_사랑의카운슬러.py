'''
오훈이에게는 지렁이 친구 N마리가 있다. 오훈이는 지렁이들을 위해 소개팅을 주선하고자 한다.

주선 방법은 임의의 지렁이 두 마리를 매칭시킨 후 한 지렁이에게 다른 지렁이가 있는 곳으로 가도록 하는 것이다.

이 때, 수학을 좋아하는 오훈이는 가능한 지렁이들이 움직인 벡터 합의 크기가 작기를 바란다.

지렁이들은 2차원 평면 안에서 이동하는데, 점 A 위에 있는 지렁이가 점 B 위에 있는 지렁이에게 갔다면 그 벡터는 점 A에서 점 B를 가리키는 벡터가 된다.

벡터 V=(x, y)의 크기는 아래와 같이 정의하자.

│V│=│(x, y)│= x * x + y * y

모든 지렁이들을 매칭시키고 소개팅을 주선하되, 각 지렁이들이 움직인 벡터를 합하여 그 크기가 최소가 되도록 하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 정수 N(2 ≤ N ≤ 20, N은 짝수) 가 주어진다.

두 번째 줄 N개의 줄에는 지렁이들이 존재하는 점의 좌표가 주어지며, 모든 지렁이는 서로 다른 위치에 있다.

모든 좌표값은 그 절대값이 100,000보다 작거나 같은 정수다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 지렁이의 움직인 벡터의 합의 크기의 최솟값을 출력하라.

'''
import sys
sys.stdin = open('1494.txt')

T = int(input())


def powerSet(x=0):
    if x == N:
        tmp = [0] * N
        for i in range(N):
            tmp[i] = temp[i]
        setLists.append(tmp)
        return
    else:
        for i in range(N):
            if i not in temp:
                temp[x] = i
                if x % 2 and check(temp, x+1):
                    temp[x] = -1
                    continue
                powerSet(x+1)
                temp[x] = -1


def check(temp, x):
    x = 0
    y = 0
    for i in range(x//2):
        a = temp[i]
        b = temp[i+1]
        x += position[a][0] - position[b][0]
        y += position[a][1] - position[b][0]
    V = x**2 + y**2
    if V > result:
        return True
    else:
        return False


for case in range(1, T+1):
    N = int(input())
    position = []
    for n in range(N):
        position.append(list(map(int, input().split())))
    temp = [-1] * N
    setLists = []
    result = 9999999999999999999
    powerSet()
    print(setLists)
