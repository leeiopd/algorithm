SIZE = 100
stack = [0] * SIZE
top = -1
def push(item):
    global top, stack
    if top >= SIZE -1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top, stack
    if top == -1:
        print("Stack is Empty!")
        return 0
    else:
        result = stack[top]
        top -= 1
        return result

push(1)
print(top, stack)
push(2)
print(top, stack)
push(3)
print(top, stack)
item = pop()
print(f'pop item => {item}')
item = pop()
print(f'pop item => {item}')
item = pop()
print(f'pop item => {item}')
print(top, stack)
# 실제 stack의 데이터는 지워지지 않고 top의 위치가 변경되어 다음 데이터를 덮어쓰면서 작동함.