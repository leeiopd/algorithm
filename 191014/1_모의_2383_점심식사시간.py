'''
N*N 크기의 정사각형 모양의 방에 사람들이 앉아 있다.

점심을 먹기 위해 아래 층으로 내려가야 하는데, 밥을 빨리 먹기 위해 최대한 빠른 시간 내에 내려가야 한다.

방 안의 사람들은 P로, 계단 입구를 S라고 했을 때 [Fig. 1]은 사람의 위치와 계단 입구의 위치를 표시한 모습이다.


[Fig. 1]


이동 완료 시간은 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간이다.

사람들이 아래층으로 이동하는 시간은 계단 입구까지 이동 시간과 계단을 내려가는 시간이 포함된다.


    ① 계단 입구까지 이동 시간
        - 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간으로 다음과 같이 계산한다.
        - 이동 시간(분) = | PR - SR | + | PC - SC |
          (PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)

    ② 계단을 내려가는 시간
        - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
        - 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
        - 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
        - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
        - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.


사람의 위치와 계단 입구의 위치 및 계단의 길이 정보가 표시된 N*N 크기의 지도가 주어진다.

이때, 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우를 찾고,

그 때의 소요시간을 출력하는 프로그램을 작성하라.


[예시]

방의 한 변의 길이 N 이 5인 지도가 [Fig. 2]와 같이 주어진 경우를 생각해보자.

지도 내에 1 은 사람을 나타내고, 2 이상 10 이하의 숫자는 계단의 입구를 나타내며 해당 숫자는 계단의 길이를 의미한다.

[Fig. 2]에는 사람 6명이 있고, 계단은 2개가 있으며 길이는 각각 3과 5이다.
 

[Fig. 2]


다음은 이동 완료되는 시간이 최소가 되는 경우 중 하나이다.

    - 1번, 2번, 3번 사람은 길이가 3인 1번 계단을 통해 이동

    - 4번, 5번, 6번 사람은 길이가 5인 2번 계단을 통해 이동

이 경우, 모든 사람이 계단을 내려가 이동 완료하는 최소 시간은 9분이다.

다른 예시로, 한 변의 길이가 N인 방에 [Fig. 3]과 같이 배치되어 있는 경우를 생각해보자.

지도 내에 1 은 사람을 나타내고, 2 이상 10 이하의 숫자는 계단의 입구를 나타내며 해당 숫자는 계단의 길이를 의미한다.

[Fig. 3]


다음은 이동이 완료되는 시간이 최소가 되는 경우 중 하나이다.

    - 1번, 2번, 3번, 4번 사람은 길이가 2인 1번 계단을 통해 이동

    - 5번, 6번 사람은 길이가 5인 2번 계단을 통해 이동


이 경우, 모든 사람이 계단을 내려가 이동 완료하는 최소 시간은 8분이다.


[제약 사항]

1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 3초

2. 방의 한 변의 길이 N은 4 이상 10 이하의 정수이다. (4 ≤ N ≤ 10)

3. 사람의 수는 1 이상 10 이하의 정수이다. (1 ≤ 사람의 수 ≤ 10)

4. 계단의 입구는 반드시 2개이며, 서로 위치가 겹치지 않는다.

5. 계단의 길이는 2 이상 10 이하의 정수이다. (2 ≤ 계단의 길이 ≤ 10)

6. 초기에 입력으로 주어지는 사람의 위치와 계단 입구의 위치는 서로 겹치지 않는다.


[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 방의 한 변의 길이 N이 주어진다.

다음 N줄에는 N*N 크기의 지도의 정보가 주어진다.

지도에서 1은 사람을, 2 이상은 계단의 입구를 나타내며 그 값은 계단의 길이를 의미한다.


[출력]

테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.

각 줄은 "#x"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)

정답은 이동이 완료되는 최소의 시간을 출력한다.

'''
import sys
sys.stdin = open('2383.txt')

T = int(input())


def Perm(cnt=0, Atemp=[], Btemp=[]):
    if cnt == L:
        if Atemp and Btemp:
            Atemp.sort()
            Btemp.sort()
            if Atemp not in stairA and Btemp not in stairB:
                stairA.append(Atemp)
                stairB.append(Btemp)
                return
        return

    X = peopleList[cnt][0]
    Y = peopleList[cnt][1]

    AL = abs(X - stairList[0][0]) + abs(Y - stairList[0][1])

    Perm(cnt+1, Atemp+[AL], Btemp)

    Perm(cnt+1, Atemp, Btemp+[AL])

    BL = abs(X - stairList[1][0]) + abs(Y - stairList[1][1])
    Perm(cnt+1, Atemp+[BL], Btemp)
    Perm(cnt+1, Atemp, Btemp+[BL])


for case in range(1, T+1):
    N = int(input())

    maps = []

    for n in range(N):
        maps.append(list(map(int, input().split())))
    RESULT = 999999999999999999999

    peopleList = []
    stairList = []
    for y in range(N):
        for x in range(N):
            if maps[y][x]:
                if maps[y][x] == 1:
                    peopleList.append([x, y])
                else:
                    stairList.append([x, y])
    L = len(peopleList)
    stairA = []
    stairB = []
    Perm()

    for i in range(len(stairA)):
        Alist = []
        for j in range(len(stairA[i])):
            Alist.append(stairA[i][j])
        Blist = []
        for j in range(len(stairB[i])):
            Blist.append(stairB[i][j])
        CNT = L
        ANS = 0
        AStairLine = []
        BStairLine = []
        while CNT:
            ANS += 1
            if ANS > RESULT:
                break
            if AStairLine:
                for j in range(len(AStairLine)):
                    AStairLine[j] -= 1
                while AStairLine:
                    if AStairLine[0] == 0:
                        AStairLine.pop(0)
                        CNT -= 1
                    else:
                        break
            if BStairLine:
                for j in range(len(BStairLine)):
                    BStairLine[j] -= 1
                while BStairLine:
                    if BStairLine[0] == 0:
                        BStairLine.pop(0)
                        CNT -= 1
                    else:
                        break
            if Alist:
                for j in range(len(Alist)):
                    Alist[j] -= 1
                if not AStairLine or (AStairLine and len(AStairLine) < 3):
                    while Alist:
                        if Alist[0] < 1 and len(AStairLine) < 3:
                            Alist.pop(0)
                            AStairLine.append(3)
                        else:
                            break
            if Blist:
                for j in range(len(Blist)):
                    Blist[j] -= 1
                if not BStairLine or (BStairLine and len(BStairLine) < 3):
                    while Blist:
                        if Blist[0] < 1 and len(BStairLine) < 3:
                            Blist.pop(0)
                            BStairLine.append(3)
                        else:
                            break

        if ANS < RESULT:
            RESULT = ANS
            print(stairA[i], stairB[i], RESULT)
    print(RESULT)
