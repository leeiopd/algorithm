import sys
sys.stdin = open("테이프이어붙이기.txt")

''''
N개의 테이프 조각이 있다. (N은 짝수) 
이것을 N/2개씩 둘로 나눠서 각 조각을 이어붙인 긴 길이의 테이프를 만들려고 한다.
(이 때 긴 길이의 테이프는 각 조각의 길이를 더한 길이를 갖는다.)
되도록이면 두 긴 테이프의 길이 차이가 최소가 되도록 만들고 싶다.
두 테이프의 길이 차이를 최소로 만들때, 두 테이프의 길이 차이를 출력하다.
 
첫번째 줄에는 테이프 조각의 갯수 N이 주어진다. (2<=N<=20, 짝수)
두번째 줄에는 N개의 테이프 조각의 길이가 주어진다. (1<=길이<=500)
같은 길이의 조각이 여러개 존재할 수 있다.

두 테이프의 길이 차이를 최소로 만들때, 두 테이프의 길이 차이를 출력하다.
'''
N = int(input())
tapes = list(map(int, input().split()))
set_list = [0] * N

def make_set(k=0):
    global tapes, result

    if k == N:
        if sum(set_list) == N//2:
            A = 0
            B = 0
            for i in range(N):
                if set_list[i] == 1:
                    A += tapes[i]
                elif set_list[i] == 0:
                    B += tapes[i]
            if abs(A - B) < result:
                result = abs(A-B)

    else:
        for i in range(2):
            set_list[k] = i
            make_set(k+1)


result = 999999999999999999
make_set()
print(result)