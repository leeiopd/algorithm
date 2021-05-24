pipe = input()
level = 0
result = 0

for i in range(len(pipe)):
    if pipe[i] == '(':
        level += 1
    else:
        level -= 1
        if pipe[i-1] == '(':
            result += level
        else:
            result += 1

print(result)