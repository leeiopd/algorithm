'''
* DFS 순열 연습
1, 2, 3 구슬이 있다.
3개의 구슬을 순서를 고려하여 3개를 고르는 모든 경우의 수를 인쇄한다.
나올수 있는 경우의 수는 다음과 같이 6가지가 된다.
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

3개의 구슬중 3개를 순서를 고려하여 고른 결과를 출력한다.
'''
import sys

sys.stdin = open("5_input.txt")

N = int(input())
result = [-99] * N
index = -1

def game():
    global result, index

    if index == N-1:
        for r in result:
            print(r, end=" ")
        print()
        return

    for i in range(1, 4):
        if i not in result:
            index += 1
            result[index] = i
            game()
            result[index] = -99
            index -= 1

game()
