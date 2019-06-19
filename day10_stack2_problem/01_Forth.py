import sys

sys.stdin = open("01_input.txt")

T = int(input())

def formula(a, b, c):
    if c == '*':
        answer = a * b
    elif c == '/':
        if b == 0:
            return
        else:
            answer =  a // b
    elif c == '+':
        answer =  a + b
    elif c == '-':
        answer =  a - b
    return answer

for case in range(1, T+1):
    code = list(input().split())
    nums = []
    result = 'error'
    for c in code:
        if c == '.':
            if len(nums) != 1:
                break
            result = nums.pop()
        
        if c.isdecimal():
            c = int(c)
            nums.append(c)
        else:
            if len(nums) > 1:
                b = nums.pop()
                a = nums.pop()
                if formula(a, b, c):
                    nums.append(formula(a, b, c))
                else:
                    break
            else:
                break
    print(f'#{case} {result}')