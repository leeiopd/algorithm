import sys

N = int(sys.stdin.readline())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
    
nums.sort()

for i in range(N):
    print(nums[i])