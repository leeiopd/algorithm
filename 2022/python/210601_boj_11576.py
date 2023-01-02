A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))[::-1]

numA = 0

for i in range(len(nums)):
    numA += nums[i] * (A ** i)

result = []
while numA != 0:
    result.append(numA % B)
    numA //= B

print(" ".join(map(str, result[::-1])))
