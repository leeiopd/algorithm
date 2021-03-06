'''
구술을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.

구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.

( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )






게임의 규칙은 다음과 같다.

① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.

② 벽돌은 숫자 1 ~ 9 로 표현되며,

   구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.



아래는 벽돌에 적힌 숫자와, 구술이 명중했을 시 제거되는 범위의 예이다.





③ 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.



예를 들어 아래와 같이 4 번 벽돌에 구술이 명중할 경우,





9번 벽돌은 4 번 벽돌에 반응하여,





동시에 제거된다.





④ 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.







N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.

N, W, H, 그리고 벽돌들의 정보가 주어질 때,

▶ 남은 벽돌의 개수를 구하라!



※ sample input 1



N = 3, W = 10, K = 10 이고 벽돌들의 정보가 아래와 같을 때,





최대한 많은 벽돌을 깨트리는 방법은 아래와 같으며, 정답은 12 가 된다.

그림의 빨간 색 원은 구술이 명중한 위치이며, 주황색 칸은 폭발의 범위를 의미한다.



i) 첫 번째 구술





ii) 두 번째 구술





iii) 세 번째 구술





[제약 사항]

1. 1 ≤ N ≤ 4

2. 2 ≤ W ≤ 12

3. 2 ≤ H ≤ 15



[입력]

가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,

그 다음 줄부터 T 개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,

다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.



[출력]

출력은 #t 를 찍고 한 칸 띄운 다음 정답을 출력한다.

(t 는 테스트 케이스의 번호를 의미하며 1 부터 시작한다)
'''
# ▶ 남은 벽돌의 개수를 구하라!
import sys
sys.stdin = open('5656.txt')

T = int(input())


# 벽돌의 폭팔을 진행하는 함수
def game(w, h, K):
    global Bcnt
    # 위치의 벽돌이 존재 할 때(벽돌이 없지만 폭팔 범위에 포함 될 때의 조건을 제외하기 위함)
    if copy[h][w]:
        Bcnt += 1
        copy[h][w] = 0
    # 폭팔 범위까지 DFS로 동작
    for k in range(1, K):
        uH = h-k
        dH = h+k
        rW = w+k
        lW = w-k
        if uH >= 0:
            game(w, uH, copy[uH][w])
        if dH < H:
            game(w, dH, copy[dH][w])
        if lW >= 0:
            game(lW, h, copy[h][lW])
        if rW < W:
            game(rW, h, copy[h][rW])


# 폭팔 함수 실행 후 맵을 정리하는 함수
def clear():
    for w in range(W):
        for h in range(H-1, 0, -1):
            if copy[h][w] == 0:
                for j in range(h - 1, -1, -1):
                    if copy[j][w]:
                        copy[h][w] = copy[j][w]
                        copy[j][w] = 0
                        break


for case in range(1, T+1):
    # N 구슬

    N, W, H = map(int, input().split())
    maps = []
    for h in range(H):
        maps.append(list(map(int, input().split())))

    brickCnt = 0

    for y in range(H):
        for x in range(W):
            if maps[y][x]:
                brickCnt += 1

    queue = [[maps, 0, 0]]
    maxBreakCnt = 0
    while queue:
        state, ballCnt, breakCnt = queue.pop()

        # 맵의 모든 벽돌 claer 했을때 종료 조건
        if breakCnt == brickCnt:
            maxBreakCnt = breakCnt
            break

        # 모든 구슬을 다 사용 했을때 종료 조건
        if ballCnt == N:
            if breakCnt > maxBreakCnt:
                maxBreakCnt = breakCnt

        else:
            for x in range(W):
                for y in range(H):
                    # 구슬을 발사할 벽돌 발건
                    if state[y][x]:
                        # 다음 상태를 위한 맵 복사
                        copy = [[0 for w in range(W)] for h in range(H)]
                        for h in range(H):
                            for w in range(W):
                                copy[h][w] = state[h][w]
                        # 벽돌의 숫자가 1일 때
                        if state[y][x] == 1:
                            copy[y][x] = 0
                            Bcnt = 1
                        # 벽돌의 숫자가 1보다 클 때
                        else:
                            Bcnt = 0
                            # DFS 시작
                            game(x, y, state[y][x])
                            # 벽돌 정리
                            clear()
                        # 상태 저장
                        queue.append([copy, ballCnt + 1, breakCnt + Bcnt])
                        # 다음 x 좌표 이동
                        break
    result = brickCnt - maxBreakCnt
    print('#{} {}'.format(case, result))
