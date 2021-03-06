'''
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110
'''
import sys

sys.stdin = open("01_input.txt")

bool_table = {'0':'0000',
              '1':'0001',
              '2':'0010',
              '3':'0011',
              '4':'0100',
              '5':'0101',
              '6':'0110',
              '7':'0111',
              '8':'1000',
              '9':'1001',
              'A':'1010',
              'B':'1011',
              'C':'1100',
              'D':'1101',
              'E':'1110',
              'F':'1111',
              }
T = int(input())
for case in range(1, T+1):
    N, nums = map(str, input().split())
    N = int(N)
    print(f'#{case} ', end='')
    for n in range(N):
        print(bool_table[nums[n]], end='')
    print()