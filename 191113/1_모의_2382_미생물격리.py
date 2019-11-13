'''
   ① 최초 각 미생물 군집의 위치와 군집 내 미생물의 수, 이동 방향이 주어진다. 약품이 칠해진 부분에는 미생물이 배치되어 있지 않다. 이동방향은 상, 하, 좌, 우 네 방향 중 하나이다.

   ② 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.

   ③ 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다. 
       미생물 수가 홀수인 경우 반으로 나누어 떨어지지 않으므로, 다음과 같이 정의한다.
       살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
       따라서 군집에 미생물이 한 마리 있는 경우 살아남은 미생물 수가 0이 되기 때문에, 군집이 사라지게 된다,

   ④ 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다. 
       합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다. 
       합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.
     

M 시간 동안 이 미생물 군집들을 격리하였다. M시간 후 남아 있는 미생물 수의 총합을 구하여라.

[제약사항]

1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 5초

2. 구역의 모양은 정사각형으로 주어지며, 한 변의 셀의 개수 N은 5이상 100이하의 정수이다. (5 ≤ N ≤ 100)

3. 최초 배치되어 있는 미생물 군집의 개수 K는 5이상 1,000이하의 정수이다. (5 ≤ K ≤ 1,000)

4. 격리 시간 M은 1이상 1,000이하의 정수이다. (1 ≤ M ≤ 1,000)

5. 최초 약품이 칠해진 가장자리 부분 셀에는 미생물 군집이 배치되어 있지 않다.

6. 최초에 둘 이상의 군집이 동일한 셀에 배치되는 경우는 없다.

7. 각 군집 내 미생물 수는 1 이상 10,000 이하의 정수이다.

8. 군집의 이동방향은 상하좌우 4방향 중 한 방향을 가진다. (상: 1, 하: 2, 좌: 3, 우: 4)

9. 주어진 입력으로 진행하였을 때, 동일한 셀에 같은 미생물 수를 갖는 두 군집이 모이는 경우는 발생하지 않는다.

10.  각 군집의 정보는 세로 위치, 가로 위치, 미생물 수, 이동 방향 순으로 주어진다. 각 위치는 0번부터 시작한다.


[입력]

첫 줄에는 총 테스트 케이스의 개수 T가 주어진다.

그 다음 줄부터 T개의 테스트 케이스가 차례대로 주어진다.

각 테스트 케이스의 첫째 줄에는 구역의 한 변에 있는 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K가 순서대로 주어지며, 다음 K줄에 걸쳐서 미생물 군집 K개의 정보가 주어진다.

미생물 군집의 정보는 세로 위치, 가로 위치, 미생물 수, 이동 방향 순으로 4개의 정수가 주어진다.


[출력]

테스트 케이스의 개수 만큼 T개의 줄에 각 테스트 케이스에 대한 답을 출력한다.

각 줄은 “#x”로 시작하고, 공백을 하나 둔 후 정답을 출력한다. (x는 테스트 케이스의 번호이며, 1번부터 시작한다.)

출력해야 할 정답은 M시간 후 남아 있는 미생물 수의 총 합이다.
'''
import sys
sys.stdin = open('2382.txt')

T = int(input())

for case in range(1, T+1):
    # N : 셀 갯수
    # M : 격리시간
    # K : 미생물 군집 갯수
    N, M, K = map(int, input().split())
    position = []
    amounts = []
    directions = []
    for k in range(K):
        # x, y, 미생물수, 이동방향
        # 1: 상, 2: 하, 3: 좌, 4: 우
        y, x, amount, D = map(int, input().split())
        position.append([x, y])
        amounts.append(amount)
        directions.append(D)

    cnt = 0

    while cnt < M:
        cnt += 1
        for i in range(K):
            if position[i]:
                if directions[i] == 1:
                    position[i][1] -= 1

                elif directions[i] == 2:
                    position[i][1] += 1

                elif directions[i] == 3:
                    position[i][0] -= 1

                else:
                    position[i][0] += 1

        for i in range(K):
            if position[i]:
                if position[i][0] == 0 or position[i][0] == N-1 or position[i][1] == 0 or position[i][1] == N-1:
                    if amounts[i] == 1:
                        position[i] = 0
                        amounts[i] = 0
                        directions[i] = 0
                    elif amounts[i] % 2:
                        amounts[i] = (amounts[i] - 1)//2
                    else:
                        amounts[i] = amounts[i] // 2

                    if directions[i] == 1:
                        directions[i] = 2
                    elif directions[i] == 2:
                        directions[i] = 1
                    elif directions[i] == 3:
                        directions[i] = 4
                    else:
                        directions[i] = 3
        for i in range(K):
            if position[i]:
                flag = 0
                temp = 0
                for j in range(K):
                    if i != j and position[i] == position[j] and amounts[i] < amounts[j]:
                        flag = 1
                        temp += amount[i]
                        amount[i] = 0
                if flag:
                    position[i] = 0
                    directions[i] = 0
                    amounts[i] = 0
    print('#{} {}'.format(case, sum(amounts)))
