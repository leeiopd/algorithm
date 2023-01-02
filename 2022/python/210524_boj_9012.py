N = int(input())

for _ in range(N):
    PS = input()
    level = 0
    for i in range(len(PS)):
        if PS[i] == '(':
            level += 1
        else:
            level -= 1
            if level < 0:
                break
    if level:
        print("NO")
    else:
        print("YES")