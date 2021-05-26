import sys
string = sys.stdin.readline().rstrip('\n')

N = int(sys.stdin.readline())
stackL = list(string)
stackR = []

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L':
        if not stackL: continue
        stackR.append(stackL.pop())
    elif order[0] == 'D':
        if not stackR: continue
        stackL.append(stackR.pop())
    elif order[0] == 'B':
        if not stackL: continue
        stackL.pop()
    elif order[0] == 'P':
        stackL.append(order[1])
        
print("".join(stackL+stackR[::-1]))