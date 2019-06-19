import sys
sys.stdin = open("2.txt")

T = int(input())

def distance(v):
    global D

    for i in range(N):
        if i == v:
            D[i] = 0



for case in range(1, T+1):
    row_by_row = list(map(int, input().split()))
    N = row_by_row.pop(0)
    maps = []
    for i in range(N):
        maps.append(row_by_row[i*N:i*N+N])

    D = [0] * N

    for n in range(N):


