'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.

카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''

import sys

sys.stdin = open("03_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    count = int(input())        # 카드개수
    nums = input()              # 숫자카드
    lists = [0] * 10            # 카운팅 배열

    for n in nums:              # 카드 숫자 순으로 갯수 정렬
        n = int(n)
        lists[n] += 1

    num_count = 0               # 가장 많은 카드 개수
    num_max = 0                 # 가장 많은 카드의 숫자

    for num in range(len(lists)-1, -1, -1):     # 정렬된 카드를 역으로 탐색하여 숫자 큰 카드부터 인덱싱 하고
        if num_count < lists[num]:              # 카드의 수가 더 많을 때의 기준으로 답 추출.
            num_max = num
            num_count = lists[num]

    print(f'#{test_case} {num_max} {num_count}')
