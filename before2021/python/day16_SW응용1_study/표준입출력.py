import sys

sys.stdin = open('1_input.txt')

num = int(input())
print(num)

a, b = map(int, input().split())
print(a, b)

for i in range(5):
    nums = map(int, input())
    for n in nums:
        print(n, end="")
    print()