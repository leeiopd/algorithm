'''
0과 1로만 이루어진 2차원 배열이 주어질 때, 왼쪽부터 연속된 1의 개수를 기록하여 배열 내용을 정리하는 프로그램을 작성하라.
예를 들어, 아래와 같은 2차원 배열이 주어졌을 때



첫 번째 줄에 행(Y), 열(X)의 값이 공백으로 구분되어 입력된다. (3≤X,Y≤1,000)
두 번째 줄부터 Y줄에 걸쳐서 X개의 숫자(0 or 1)가 입력된다.

정리된 배열 내용을 출력한다.
'''
import sys

sys.stdin = open("A4_input.txt")


Y, X = map(int, input().split())
maps = []

for y in range(Y):
    x_list = list(map(int, input().split()))
    maps.append(x_list)

for y in range(Y):
    add = 0
    for x in range(X):
        if maps[y][x] == 1:
            add += 1        
            maps[y][x] = add
        else:
            add = 0

for y in range(Y):
    result = ' '.join(map(str, maps[y]))
    print(result)