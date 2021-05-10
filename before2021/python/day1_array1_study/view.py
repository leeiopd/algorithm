import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    n = int(input())
    structs = list(map(int, input().split()))

    result = 0
    for k in range(2, n-2):
        a = structs[k] - structs[k - 2]
        b = structs[k] - structs[k - 1]
        c = structs[k] - structs[k + 1]
        d = structs[k] - structs[k + 2]
        if a >= 1 and b >= 1 and c >= 1 and d >= 1:
            lists = [a, b, c, d]
            mem = lists[0]
            print(lists)
            print(mem)
            for num in range(0, 4):
                if mem >= lists[num]:
                    mem = lists[num]
            print(result)
            print(mem)
            result += mem
            print(k, result)
    print(k, result)


