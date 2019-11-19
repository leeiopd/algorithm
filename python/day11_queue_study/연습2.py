Q = []

Q.append(1)
Q.append(2)
Q.append(3)

print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))

if Q:
    print(Q.pop(0))
else:
    print('Q is Empty')
print(Q)