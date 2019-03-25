import sys

sys.stdin = open("2_input.txt")
'''
첫 번째 줄에 N(1≤N≤50,000)이 주어진다. N은 정렬되어 주어지는 데이터의 수이다.
두 번째 줄에는 N개의 서로 다른 수가 정렬되어 주어진다. 각 수는 공백 하나로 분리되어 주어진다.
세 번째 줄에는 데이터에서 찾아야 할 특정한 수의 개수 T(1≤T≤10,000)가 주어진다. 즉, T가 3이면 3개의 수를 정렬된 데이터에서 찾아야 한다.
네 번째 줄에는 T개의 수가 공백 하나로 분리되어 주어진다.

찾아야 할 수가 정렬되어 주어진 데이터의 수 중에서 앞에서부터 몇 번째에 있는지 그 위치를 출력한다.
첫 번째 위치는 1이다. 만약, 찾으려는 수가 주어지는 데이터에 존재하지 않는다면, 0을 출력한다.
'''

N = int(input())

nums = list(map(int, input().split()))

T = int(input())
T_nums = list(map(int, input().split()))

def find_num(t, s, e):
    m = (s+e)//2

    if nums[s] == t:
        return print(s+1)
    elif nums[e] == t:
        return print(e+1)
    elif nums[m] == t:
        return print(m+1)
    elif m == e-1 or s == m:
        return print(0)

    if t > nums[m]:
        find_num(t, m, e)
    elif t < nums[m]:
        find_num(t, s, m)



for t in T_nums:
    find_num(t, 0, len(nums)-1)
