import sys
sys.stdin = open("도자기.txt")
'''
여러종류의 흙의 재료 N개를 가지고 있다. 
N개의 흙의 재료중에서 M개 만큼의 재료를 섞어서 다양한 종류의 도자기를 만들려고 한다. 
몇가지 종류의 도자기를 만들수 있는지를 구한다
이때 재료를 섞는 순서는 상관 없으며 넣는 재료의 비율만이 도자기의 종류를 결정한다.
예로 흙의 재료 5개 1 1 2 3 3 재료가 주어지고 이중 2개의 재료를 사용하여 만들수 있는 도자기의 종류는 (1 1), (1 2), (1 3), (2 3), (3 3)해서 5가지의 도자기를 만들수 있다. 
N, M는 최대 12개이며, M은 N과 같거나 작을수 있다.
흙의 재료는 26가지로 1~26까지로 표현한다. 

첫번째 줄에 테스트케이스 T개,  두번째 줄에 흙의 종류 N개와 흙을 섞을수 있는 개수 M개가 주어진다. 
세번째 줄에 흙의 종류 N개의 데이타가 주어진다. 

몇가지 종류의 도자기를 만들수 있는지를 구한다
'''
T = int(input())

def make_china(k=0):
    global vixited, result
    if k == N:
        mix = [0] * M
        top = 0
        if sum(set_list) == M:
            for i in range(N):
                if set_list[i] == 1:
                    mix[top] = muds[i]
                    top += 1
        mix.sort()
        if mix not in visited:
            visited.append(mix)
            result += 1


    else:
        for i in range(2):
            set_list[k] = i
            make_china(k+1)


for case in range(1, T+1):
    N, M = map(int, input().split())
    muds = list(map(int, input().split()))
    set_list= [0] * N
    result = 0
    visited= []
    make_china()
    print(result-1)
