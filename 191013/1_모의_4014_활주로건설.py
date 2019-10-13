'''
[Fig. 1] 과 같은 N * N 크기의 절벽지대에 활주로를 건설하려고 한다.

각 셀의 숫자는 그 지형의 높이를 의미한다.



활주로를 [Fig. 2] 와 같이 가로 또는 세로 방향으로 건설할 수 있는 가능성을 확인하려고 한다.




활주로는 높이가 동일한 구간에서 건설이 가능하다.

높이가 다른 구간의 경우 활주로가 끊어지기 때문에 [Fig. 3] 과 같은 경사로를 설치해야만 활주로를 건설 할 수 있다.





경사로는 길이가 X 이고, 높이는 1 이다.

경사로는 높이 차이가 1 이고 낮은 지형의 높이가 동일하게 경사로의 길이만큼 연속되는 곳에 설치 할 수 있다.



예를 들어 [Fig. 4] 는 길이가 2 이고 높이가 1 인 경사로를 설치하는 예를 보여준다.





경사로의 길이 X 와 절벽지대의 높이 정보가 주어질 때,

활주로를 건설할 수 있는 경우의 수를 계산하는 프로그램을 작성하라.





[예시]

지도의 한 변의 크기 N 이 6, 경사로의 길이 X 가 2 일 때,

[Fig. 5] 와 같이 지형의 높이가 주어진 경우를 생각해 보자.





[Fig. 5] 의 지형 중 [ 3, 3, 3, 2, 1, 1 ] 의 경우 [Fig. 6] 과 같이 높이 2 인 구간이 경사로 길이보다 짧아서 활주로를 설치 할 수 없다.




[ 3, 3, 3, 2, 2, 1 ] 의 지형은 [Fig. 7] 과 같이 경사로를 지형 밖까지 설치해야 되기 때문에 활주로를 설치할 수 없다.




[ 2, 2, 3, 2, 2, 2 ] 지형과 [ 3, 3, 3, 2, 2, 2 ] 지형의 경우 아래 [Fig. 8-1], [Fig. 8-2] 와 같이 경사로를 설치하여 활주로를 건설할 수 있다.




[Fig. 5] 와 같은 지형에 활주로를 건설하는 방법은

아래 [Fig. 9] 와 같이 총 7 가지 ( 가로 방향 3 가지, 세로 방향 4 가지 ) 경우가 있다.

즉, 예제에 대한 정답은 7 이 된다




[제약사항]

1. 시간제한 : 최대 50 개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3 초

2. N 의 크기는 6 이상 20 이하의 정수이다. ( 6 ≤ N ≤ 20 )

3. 경사로의 높이는 항상 1 이고, 길이 X 는 2 이상 4 이하의 정수이다. ( 2 ≤ X ≤ 4 )

4. 지형의 높이는 1 이상 6 이하의 정수이다.

5. 동일한 셀에 두 개 이상의 경사로를 겹쳐서 사용할 수 없다.

( 아래 [Fig. 10] 과 같은 경우는 경사로를 설치하여 활주로를 연결 할 수 없다. )




6. 경사로는 세워서 사용할 수 없다. ( [Fig. 11] 참고 )






[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,

그 다음 줄부터 T 개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 크기인 N 과 경사로의 길이 X 가 주어진다.

다음 N 개의 줄에는 N * N 크기의 지형 정보가 주어진다.





[출력]

테스트 케이스 개수만큼 T 개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t" 로 시작하고 공백을 하나 둔 다음 정답을 출력한다. ( t 는 1 부터 시작하는 테스트 케이스의 번호이다. )

정답은 활주로를 건설할 수 있는 경우의 수이다.
'''
import sys
sys.stdin = open('4014.txt')

T = int(input())


def Check(line):

    # 한줄의 모든 높이가 같을 때
    ave = sum(line)//N
    aveFlag = 1
    for n in range(N):
        if line[n] != ave:
            aveFlag = 0
            break

    if aveFlag:
        return True

    # 경사로 중복 좌표 확인
    temp = []

    # 올라가는길
    for i in range(1, N):
        # 이전 위치보다 높아졌을 때
        if line[i-1] < line[i]:
            # 경사로를 놓을 공간이 없음
            if i < X:
                return False

            # 높이의 차이가 1
            if line[i-1] == line[i] - 1:
                # 경사로 설치 위치 저장
                temp.append(i-1)
                for j in range(X, 1, -1):
                    # 경사로를 설치 가능 공간 확인
                    if i-j < 0:
                        return False

                    # 경사로를 설치 할 위치의 높이가 동일한지 확인
                    if line[i-1] != line[i-j]:
                        return False

                    # 경사로 설치 위치 저장
                    temp.append(i-j)
            else:
                return False

    # 내려가는 길
    for i in range(1, N):
        # 이전 위치보다 낮아 졌을 때
        if line[i-1] > line[i]:

            # 경사로를 놓을 공간 확인
            if N-i < X:
                return False

            # 이전 위치와의 높이 차가 1 인것을 확인
            if line[i-1] - 1 == line[i]:
                for j in range(1, X):
                    # 경사로 설치 공간 확인
                    if i+j >= N:
                        return False

                    # 경사로를 설치할 곳의 높이가 모두 동일한지 확인
                    if line[i] != line[i+j]:
                        return False

                    # 경사로를 놓을 자리가 비어있는지 확인
                    if i+j in temp:
                        return False
            else:
                return False
    return True


for case in range(1, T+1):
    N, X = map(int, input().split())

    maps = []

    for n in range(N):
        maps.append(list(map(int, input().split())))

    # 가로줄 복사
    copy1 = [0] * N

    # 세로줄 복사
    copy2 = [0] * N
    result = 0

    for y in range(N):
        for x in range(N):
            copy1[x] = maps[y][x]
            copy2[x] = maps[x][y]

        # 가로줄 확인
        if Check(copy1):
            result += 1

        # 세로줄 확인
        if Check(copy2):
            result += 1

    print('#{} {}'.format(case, result))
