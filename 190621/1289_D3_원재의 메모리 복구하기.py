'''
원재가 컴퓨터를 만지다가 실수를 저지르고 말았다. 메모리가 초기화된 것이다.

다행히 원래 메모리가 무슨 값이었는지 알고 있었던 원재는 바로 원래 값으로 되돌리려고 했으나 메모리 값을 바꿀 때 또 문제가 생겼다.

메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.

예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.

원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 메모리의 원래 값이 주어진다.

메모리의 길이는 1이상 50이하이다.

[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

초기값(모든bit가 0)에서 원래 값으로 복구하기 위한 최소 수정 횟수를 출력한다.
'''
import sys

sys.stdin = open('1289.txt')

T = int(input())

def check(nums):
    cnt = 0
    for n in nums:
        if n == '1':
            cnt += 1
    if cnt != 0:
        return 1
    else:
        return 0

for case in range(1, T+1):
    nums = list(input())
    
    cnt = 0
    while check(nums):
        cnt += 1
        for i in range(len(nums)):
            if nums[i] == '1':
                for j in range(i, len(nums)):
                    if nums[j] == '1':
                        nums[j] = '0'
                    else:
                        nums[j] = '1'
                break
    print(f'#{case} {cnt}')