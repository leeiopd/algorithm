import sys
sys.stdin = open("퍼킷.txt")
'''
퍼킷은 유명하고 맛있는 음식이다.
퍼킷을 만들기 위해서는 재료를 신중하게 골라야 한다.
신은 N개의 재료를 갖고 있으며 각각의 재료의 신맛의 정도 S와 쓴맛의 정도 B를 알고 있다.
주어진 재료로 퍼킷을 만들 경우, 퍼킷의 신맛은 재료 각각의 신맛 정도의 곱이고,
퍼킷의 쓴맛은 재료 각각의 쓴맛 정도의 합으로 나타낼 수 있다.
퍼킷이 맛있어 지려면 신맛의 정도와 쓴맛의 정도의 차이가 작을수록 맛있어진다.
N개의 재료가 주어질 때 최고의 퍼킷을 만들어 보라.

첫 번째 줄에는 재료 개수 N(2≤N≤10)이 입력 된다.
두 번째 줄부터 N+1 번째 줄에는 각 재료의 신맛 정도 S와 쓴맛 정도 B가 입력된다.
B와 S는 모두 1,000,000,000 보다 작은 양의 정수이다.

주어진 재료로 만들 수 있는 최고 퍼킷의 신맛과 쓴맛의 차이를 출력하라.
'''

def perm(k=0, ssum_S=0, ssum_B=0):
    global result, set_list
    if k == N:
        if 1 not in set_list:
            return
        add_s = 1
        add_b = 0
        for i in range(N):
            if set_list[i] == 1:
                add_s *= S_list[i]
                add_b += B_list[i]
        teast = abs(add_s - add_b)
        if teast < result:
            result = teast

    
    else:

        set_list[k] = 1
        perm(k+1, ssum_S*S_list[k], ssum_B+B_list[k])
        set_list[k] = 0
        perm(k+1, ssum_S, ssum_B)





N = int(input())

S_list = [0] * N
B_list = [0] * N
set_list = [0] * N
for n in range(N):
    S, B = map(int, input().split())
    S_list[n] = S
    B_list[n] = B
result = 99999999999999999999
perm()
print(result)