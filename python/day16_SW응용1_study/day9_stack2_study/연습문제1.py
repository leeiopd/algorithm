formula = '2+3*4/5'
stack = []
for f in formula:
    if f.isdecimal():   # .isdecimal,
        print(f, end='')
    else:
        stack.append(f)

while len(stack) > 0:
    print(stack.pop(), end='')

