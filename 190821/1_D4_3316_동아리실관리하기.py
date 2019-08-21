'''
삼성초등학교에는 영준, 준환, 동한, 하니 이렇게 네 명이 프로그래밍 동아리에 속해있다. 부원 네 명의 이름을 편의상 A, B, C, D라고 하자.

앞으로 N일간의 활동 일정을 정해야 한다.

각 부원은 하루의 활동에 참여를 할지 하지 않을지를 정해야 하며, 어떤 부원이 참여하는지의 경우의 수는 하루에 총 16가지이다.

그런데 아무도 활동에 참여하지 않으면 동아리가 폐부 될 수 있으므로 아무도 참여를 하지 않아서는 곤란하다.

즉 실제로는 15가지 경우가 있다.

동아리 실을 여는 열쇠는 하나밖에 없고 활동이 끝나면 동아리 실을 잠가야 하기 때문에 문을 열어주기 위해 열쇠를 가진 사람은 무조건 활동에 참여해야 한다.

오늘 활동에 참여하는 사람 중에 내일 활동에도 참여하는 사람이 있다면 열쇠를 넘겨줄 수 있다.

첫 번째 날에는 A가 열쇠를 가지고 있다.

모든 활동이 끝난 다음에는 열쇠를 누가 가지고 있어도 상관이 없다.


또한 N일 동안 각 날마다 활동의 책임자가 있어서 이 책임자는 무조건 활동에 참여해야 한다.

N일 동안의 동아리 활동을 할 수 있는 경우의 수를 출력하는 프로그램을 작성하라.

(열쇠를 누구에게 넘겨주는지는 중요하지 않고 어떤 사람이 활동을 하는지 안 하는지에 따라 경우의 수를 세어야 한다.)

예를 들어 동아리실 담당자가 첫날에는 B, 둘째 날 C라고 해보자.

위의 그림에서 가능한 경우에는 1일차와 2일차에 A가 열쇠를 전달해 주면 된다.

하지만 불가능 한 경우에는 1일차 있었던 사람이 2일차에 아무도 없기 때문에 동아리 실을 유지할 수 없게 된다.
 

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 길이 10,000 이하인 하나의 문자열이 주어진다. 이 문자열은 A, B, C, D로 이루어져 있으며, i번째 문자는 i번째 날의 책임자가 누구인지를 나타낸다.


[출력]
각 테스트 케이스마다 N일 동안의 동아리 활동을 할 수 있는 경우의 수를 출력하는 프로그램을 작성하라.

이 수는 너무 커질 수 있으므로 1,000,000,007로 나눈 나머지를 출력한다.
'''
import sys
sys.stdin = open('3316.txt')

T = int(input())


def powerSet(x=0):
    if x == 4:
        tmp = [0] * 4
        for i in range(4):
            if temp[i]:
                tmp[i] = 1
        powerSetList.append(tmp)
    else:
        for i in range(2):
            temp[x] = i
            powerSet(x+1)


def game(x=0):
    global result
    if x == N:
        result += 1
        if result >= 1000000007:
            result -= 1000000007
    else:
        for j in range(4):
            if peopleList[x][j]:
                leader = j

        if x == 0:
            for i in range(len(powerSetList)):
                if powerSetList[i][leader] and powerSetList[i][0]:
                    resultSet.append(powerSetList[i])
                    game(x+1)
                    resultSet.pop(-1)

        else:
            for i in range(len(powerSetList)):
                if powerSetList[i][leader]:
                    flag = 0
                    for k in range(4):
                        if resultSet[-1][k]:
                            if powerSetList[i][k]:
                                flag = 1
                    if flag:
                        resultSet.append(powerSetList[i])
                        game(x+1)
                        resultSet.pop(-1)


def peopleCheck():
    while peoples:
        people = peoples.pop(0)
        if people == 'A':
            peopleList.append([1, 0, 0, 0])

        if people == 'B':
            peopleList.append([0, 1, 0, 0])

        if people == 'C':
            peopleList.append([0, 0, 1, 0])

        if people == 'D':
            peopleList.append([0, 0, 0, 1])


temp = [0] * 4
powerSetList = []
powerSet()

for case in range(1, T+1):
    peoples = list(map(str, input()))
    N = len(peoples)

    peopleList = []
    peopleCheck()

    resultSet = []
    result = 0
    game()
    result = result % 1000000007

    print('#{} {}'.format(case, result))
