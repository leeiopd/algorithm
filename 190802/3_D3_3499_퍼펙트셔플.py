'''
카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다. 

정확한 방식은 다음 그림과 같다.


N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.

만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.

두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.

카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다.

[출력]

각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.
'''
import sys
sys.stdin = open('3499.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    half = len(cards)//2
    if N % 2:
        A_set = cards[:half+1]
        B_set = cards[half+1:]
    else:
        A_set = cards[:half]
        B_set = cards[half:]
    result = []
    for i in range(half):
        result.append(A_set[i])
        result.append(B_set[i])
    if N%2:
        result.append(A_set[-1])
    print(f"#{case} {' '.join(result)}")
