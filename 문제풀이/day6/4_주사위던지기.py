'''
자연수 N과 M을 입력 받아서 주사위를 N번 던져서 나온 눈의 합이 M이 나올 수 있는 모든 경우를 출력하는 프로그램을 작성하시오.

첫 줄에 주사위를 던진 횟수 N(2≤N≤7)과 눈의 합 M(1≤M≤40)이 들어온다.

주사위를 던진 횟수의 합이 M이 되는 경우를 모두 출력한다.
작은 숫자부터 출력한다.
'''

import sys

sys.stdin = open("4_input.txt")

N, M = map(int, input().split())


num_list = [-99] * N
index = -1
def game():
    global num_list, index
    index += 1

    if index == N:
        if sum(num_list) == M:
            for i in range(N):
                print(num_list[i], end=" ")
            print()
            index -= 1
            return
        else:
            index -= 1
            return

    for i in range(1, 7):
        num_list[index] = i
        if sum(num_list) > M:
            num_list[index] = -99
            index -= 1
            return
        game()
        num_list[index] = -99
    index -= 1

game()