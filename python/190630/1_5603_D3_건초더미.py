"""
N개의 건초더미가 있다.

원래는 모든 건초더미의 크기가 같았는데, 밤새 말썽꾸러기 규호가 건초들의 위치를 여기저기 바꿔 놓아서, 이젠 건초더미들의 크기가 달라져버렸다.

바뀐 건초더미들이 주어졌을 때, 건초를 최소 몇 번 움직여야 다시 모두 같게 만들 수 있을지 구하는 프로그램을 작성하라.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 10)
각 테스트케이스마다 첫 줄에 건초더미의 개수 N이 주어진다. (1 ≤ N ≤ 10,000)
그 다음 N개의 줄에 걸쳐 각 건초더미의 크기가 주어진다. (각 건초더미의 크기는 1이상 10,000 이하의 정수)

[출력]
각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 건초더미를 모두 같게 만드는데 필요한 최소 움직임의 횟수를 출력한다. 
"""
import sys
sys.stdin = open("5603.txt")

T = int(input())

for case in range(1, T+1):
    N = int(input())
    nums = []
    for n in range(N):
        nums.append(int(input()))

    total = sum(nums)
    avr = total//N
    result = 0
    for n in nums:
        if n > avr:
            result += (n - avr)
    print("#{} {}".format(case, result))