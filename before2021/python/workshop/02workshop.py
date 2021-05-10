'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,

제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open("02_input.txt", "r")

T = 10

for test_case in range(1, T+1):
    blocks = int(input())
    long = list(map(int, input().split()))
    cnt = 0

    while cnt <= blocks:
        cnt += 1
        max_box = 0
        min_box = 100

        for i in range(len(long)):
            if long[i] > max_box:
                max_box = long[i]
                max_cnt = i

            if long[i] < min_box:
                min_box = long[i]
                min_cnt = i
        
        long[max_cnt] -= 1
        long[min_cnt] += 1
        
        if long[max_cnt] - long[min_cnt] <= 1:
            break
    result = max_box - min_box
    print(f'#{test_case} {result}')