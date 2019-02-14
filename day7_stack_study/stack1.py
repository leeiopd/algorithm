def push(item):
    s. append(item)

def pop():
    if len(s) == 0:
        print("Stack is Empty!")
        return
    else:
        return s.pop()

s = []

push(1)
print(s)
push(2)
print(s)
push(3)
print(s)
print('------------------')
print(f'pop : {pop()}')
print(s)
print(f'pop : {pop()}')
print(s)
print(f'pop : {pop()}')
print(s)