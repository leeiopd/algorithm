SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1
def isFull():
    if rear == len(Q):
        return True
    else:
        return False

def isEmpty():
    if front == rear:
        return True
    else:
        return False

def enQueue(item):
    global rear
    rear += 1
    Q[rear] = item

def deQueue():
    global front
    front += 1
    return Q[front]

def Qpeek():
    return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)

print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())

print(Q)