N = int(input())

nums = [0, 1, 2, 4]

for _ in range(4, 12):
    nums.append(sum(nums[-3:]))

for _ in range(N):
    print(nums[int(input())])
