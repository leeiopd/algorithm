'''
어떤 자연수 k가 있을 때, k의 약수가 1과 k뿐이라면 k는 소수이다.
즉, 약수가 정확히 2개만 존재하는 자연수이다. (단, 1 != k )
두 개의 자연수 a, b가 주어진다.
min(a, b) <= k <= max(a, b)인 k들 중에서
소수인 k의 개수와 min(k), max(k)를 구하는 프로그램을 작성하시오.


첫 번째 줄에 a, b가 공백으로 구분되어 입력된다.

[입력 값의 정의 역]
1 <= a, b <= 100,000

[Sub-Task Info]
- data set #1 (80%): a, b는 10,000 이하의 값이다.
- data set #2 (20%) : a, b는 100,000 이하의 값이다.
* 입력 값이 클 때, 시간초과에 걸리지 않는 알고리즘을 설계할 수 있도록 하세요.

첫 번째 줄에 소수의 개수를 출력한다.
두 번째 줄에 소수들 중 최댓값과 최솟값의 합을 출력한다.


'''
import sys

sys.stdin = open("C7_input.txt")

a, b = map(int, input().split())

if a > b:
    a, b = b, a


def isPrime(num):
    if num == 1: return False

    n = int(num**0.5)
    for k in range(2, n + 1):
        if num % k == 0: return False
    return True


result = []
for k in range(a, b + 1):
    if isPrime(k):
        result.append(k)
print(len(result))
print(result[0] + result[-1])