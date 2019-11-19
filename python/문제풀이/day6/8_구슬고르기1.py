'''
* DFS 조합 연습1
- 1, 2, 3 3개의 구슬을 0개 ~ 3개까지 골고루 조합하여 상자에 담아 본다.
- 나올수 있는 경우의 수는 다음과 같이 8가지가 된다.
1 2 3
1 2 0
1 0 3
1 0 0
0 2 3
0 2 0
0 0 3
0 0 0

* 다음 주어진 main()함수를 사용하여 DFS()함수를 완성하시오
- 구슬이 담긴 a배열이 있고 옮겨 담을 상자 b배열이 있다
- 구슬을 상자에 담을 때 구슬과 같은 위치에 담는다
- 재귀함수로 구현하고 구슬N개는 3개로 정한다.
- 출력예시와 같이 모든 조합을 인쇄한다

3개의 구슬을 0개~3개를 골고루 조합한 결과를 출력한다.
'''
N = 3

visited = [-99] * N
top = -1
result = []
def check():
    global visited, top
    if top == N-1:

        k = [0] * N
        for v in range(len(visited)):
            k[v] = visited[v]
        if k not in result:
            result.append(k)
        return

    for i in range(1, -1, -1):
        top += 1
        visited[top] = i
        check()
        visited[top] = -99
        top -= 1

check()

for r in result:
    if r[0] != 0:
        print(1, end=" ")
    else:
        print(r[0], end=" ")

    if r[1] != 0:
        print(2, end=" ")
    else:
        print(r[1], end=" ")

    if r[2] != 0:
        print(3, end=" ")
    else:
        print(r[2], end=" ")
    print()
