'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''


arr = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))


def isWall(x, y):
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return False
    else:
        return True

def calAbs(y, x):
    if y - x > 0: return y - x
    else: return x - y



dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

n_sum = 0

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]

            if isWall(testX, testY):
                n_sum += calAbs(arr[y][x], arr[testY][testX])

print(n_sum)
