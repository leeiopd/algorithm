insert = input()

top = -1
stack = []

def push(item):
    global top, stack
    stack.append(item)
    top += 1
def pop():
    global top
    if top < -1:
        return False
    else:
        top -= 1
        return stack.pop


open = '('
close = ')'
flag = True

for i in insert:
    if i == open:
        push(i)
    elif i == close:
        flag = pop()

    if flag == False:
        break

if top == -1:
    print(True)

else:
    print(False)