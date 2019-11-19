nums = list(map(int,input()))
print(nums)
c = [0] * len(nums)
result = [0]*len(nums)
for n in nums:
    c[n] += 1

for i in range(1,len(c)):
    c[i] += c[i-1]
print(c)

for num in range(len(nums)-1, -1, -1):
    result[c[nums[num]]-1] = nums[num]
    c[nums[num]] -= 1

print(result)
