'''
주어진 두 문자열의 최대 공통 부분 수열(Longest Common Sequence)의 길이를 계산하는 프로그램을 작성하시오.

예를 들어 "acaykp"와 "capcak"의 경우, 두 문자열의 최대 공통 부분 수열은 "acak"로 길이가 4이다.

최장 공통 부분문자열(Longest Common Substring)을 계산하는 것이 아님에 주의한다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫째 줄에 두 문자열이 공백을 사이에 두고 주어진다.

각 문자열은 알파벳 소문자로만 구성되어 있음이 보장된다.

각 문자열의 길이는 1,000 이하의 자연수이다.

[출력]

각 테스트 케이스마다 ‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 공통 부분 수열의 길이를 출력한다.
'''
import sys
sys.stdin = open('3304.txt')

T = int(input())


def check(an, bn):
    if an == 0 or bn == 0:
        return 0

    if


for case in range(1, T+1):
    A, B = map(str, input().split())
    result = [0]
    memo = ''
