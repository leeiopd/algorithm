nums = list(map(int, list(input())))

nums.sort(reverse=True)


def check():
    if nums[-1]:
        return -1
    s = sum(nums)
    if s % 3:
        return -1
    return "".join(list(map(str, nums)))


print(check())
