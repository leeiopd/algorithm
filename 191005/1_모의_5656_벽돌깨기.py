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
import sys
sys.stdin = open('5656.txt')

T = int(input())


def game(w, h, K):
    global Bcnt
    Bcnt += 1
    nBric[h][w] = 0
    for k in range(1, K):
        uH = h-k
        dH = h+k
        rW = w+k
        lW = w-k
        if uH >= 0 and nBric[uH][w]:
            game(w, uH, nBric[uH][w])
        if dH < H and nBric[dH][w]:
            game(w, uH, nBric[dH][w])
        if lW >= 0 and nBric[h][lW]:
            game(w, uH, nBric[h][lW])
        if rW < W and nBric[h][rW]:
            game(w, uH, nBric[h][rW])


def clear():
    for w in range(W):
        for h in range(H-1, 0, -1):
            if nBric[h][w] == 0:
                nBric[h][w] = nBric[h-1][w]
                nBric[h-1][w] = 0


for case in range(1, T+1):
    # N 구슬

    N, W, H = map(int, input().split())
    maps = []
    for h in range(H):
        maps.append(list(map(int, input().split())))

    temp = [[maps, 0, 0]]
    result = 0
    resultBrick = [[0 for w in range(W)] for h in range(H)]
    while temp:
        bric, cnt, ans = temp.pop()
        print(cnt, ans)
        if cnt > N:
            if ans > result:
                result = ans
                for y in range(H):
                    for x in range(W):
                        resultBrick[y][x] = bric[y][x]
        else:
            for w in range(W):
                for h in range(H):
                    if bric[h][w] != 0:
                        nBric = [[0 for w in range(W)] for h in range(H)]
                        for y in range(H):
                            for x in range(W):
                                nBric[y][x] = bric[y][x]
                        Bcnt = 0
                        game(w, h, nBric[h][w])
                        clear()
                        temp.append([nBric, cnt + 1, ans + Bcnt])
                        break

    checkCnt = 0
    for w in range(W):
        for h in range(H):
            if resultBrick[h][w] != 0:
                checkCnt += 1
    print(checkCnt, result)
