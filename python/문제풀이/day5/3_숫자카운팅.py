import sys

sys.stdin = open("3_input.txt")

'''
첫째 줄에 N 이 입력된다. (1≤N≤200,000)
둘째 줄에 배열에 저장 되어있는 N개의 숫자가 순서대로 공백으로 구분되어 입력된다.
셋째 줄에 M 이 입력된다. (1≤M≤200,000)
넷째 줄에 M개의 탐색할 숫자가 순서대로 공백으로 구분되어 입력된다.
(이 숫자는 정렬 되어있지 않다)

입력 넷째 줄에서 주어진 탐색할 숫자의 배열 내 저장된 개수를 차례대로 출력한다.
'''

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
def lowerSearch(s, e, where):
    global arr
    while s < e:
        # e = N-1
        # s = 0
        m = (s+e)//2 # mid
        # if where == arr[m]: return m+1
        if where > arr[m] : s = m + 1
        else: e = m
    return e

def upperSearch(s, e, where):
    global arr
    while s < e:
        # e = N-1
        # s = 0
        m = (s+e)//2 # mid
        # if where == arr[m]: return m+1
        if where >= arr[m] : s = m + 1
        else: e = m
    return e

for i in range(M):
    low = lowerSearch(0, N, find[i])
    up = upperSearch(0, N, find[i])
    if low != up: # 찾았을 경우에만 오른쪽 끝 탐색
        print(up-low, end=' ')
    else:
        print(0,end=' ')