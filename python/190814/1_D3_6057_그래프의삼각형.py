'''
정점이 N개, 간선이 M개 있는 그래프가 주어진다. 정점에는 1번에서 N번까지의 번호가 붙어 있다.

이 때, i번 정점과 j번 정점 사이에, j번 정점과 k번 정점 사이에, k번 정점과 i번 정점 사이에

모두 간선이 있는 ( i, j, k ) (단, i < j < k )를 삼각형이라고 하자.

삼각형의 개수를 구하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수  이 공백으로 구분되어 주어진다.

다음 M개의 줄에는 두 정수  이 공백으로 구분되어 주어진다.

이는 x번 정점과 y번 정점 사이에 간선이 있다는 의미이다.

반대로 y번 정점과 x번 정점 사이에 간선이 있다는 의미도 된다.

같은 간선을 의미하는 입력이 여러 번 주어지지 않는다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후,

삼각형의 개수를 출력한다.
'''
import sys
sys.stdin = open('6057.txt')

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    front_point = [0] * M
    back_point = [0] * M
    for m in range(M):
        num = list(map(int, input().split()))
        front_point[m] = num[0]
        back_point[m] = num[1]

    result = 0

    for i in range(M):
        for j in range(M):
            if back_point[i] == front_point[j]:
                for k in range(M):
                    if front_point[i] == front_point[k] and back_point[j] == back_point[k]:
                        result += 1

    print('#{} {}'.format(case, result))
