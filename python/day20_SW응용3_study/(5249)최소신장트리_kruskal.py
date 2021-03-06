import sys
sys.stdin = open('1_input.txt')
T = int(input())

def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def short():
    global result
    cnt = 0     #간선갯수
    total = 0   #가중치의 합
    i = 0       #제어변수
    while cnt < V:                      # MST 구성을 위해 V개의 간선을 선택
        p1 = findSet(route[i][1])        # 두 노드의 대표원소 알아내기
        p2 = findSet(route[i][2])
        if p1 != p2:                    # 사이클이 생성되지 않으면
            total += route[i][0]         # MST에 포함되므로 가중치 추가
            cnt += 1                    # 간선 개수 증가
            p[p2] = p1                  # 대표 원소 관리(union)
        i += 1                          # 저장된 다음 간선으로 이동
    result = total                        # MST 완성 후 가중치 합 반환


for case in range(1, T+1):
    V, E = map(int, input().split())
    route = []
    for e in range(E):
        f, t, w = map(int, input().split())
        route.append([w, f, t])                 # 가중치, 시작, 끝
    route.sort()
    p = list(range(V+1))                        # 대표원소 초기화(make set)
    short()
    print('#{} {}'.format(case, result))
