import sys
string = sys.stdin.readline().rstrip('\n')

N = int(sys.stdin.readline())
cursor = len(string)

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L':
        if cursor == 0: continue
        cursor -= 1
    elif order[0] == 'D':
        if cursor == len(string): continue
        cursor += 1
    elif order[0] == 'B':
        if cursor == 0: continue
        string = string[:cursor-1] + string[cursor:]
    elif order[0] == 'P':
        string = string[:cursor] + order[1] + string[cursor:]
        cursor += 1
        
print(string)