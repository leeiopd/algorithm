'''
한 정수 n을 입력 받아서 1부터 n까지의 합을 구하여 출력하시오.
단, 반드시 재귀함수로 구현하시오.

입력은 키보드로부터 이루어진다.
정수 n(2 ≤ n ≤ 500)이 첫 번째 줄에 입력된다.


'''
import sys

sys.stdin = open("1_input.txt")

N = int(input())
cnt = 0
result = 0
def add(N):
    global cnt, result
    if cnt == N:
        return
    cnt += 1
    result += cnt
    add(N)

add(N)
print(result)