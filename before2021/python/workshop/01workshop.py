'''
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여,

강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다.

따라서 답은 6이 된다.
'''
import sys

sys.stdin = open("01_input.txt", "r")

T = 10
for tc in range(T):
    n = int(input())
    structs = list(map(int, input().split()))

    result = 0
    for k in range(2, n-2):
        a = structs[k] - structs[k - 2]
        b = structs[k] - structs[k - 1]
        c = structs[k] - structs[k + 1]
        d = structs[k] - structs[k + 2]
        if a >= 1 and b >= 1 and c >= 1 and d >= 1:
            lists = [a, b, c, d]
            mem = lists[0]

            for num in range(0, 4):
                if mem >= lists[num]:
                    mem = lists[num]

            result += mem

    print(f'#{tc+1} {result}')
