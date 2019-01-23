'''
2차 배열을 초기화 한 후 2차배열 형태로 출력하시오

입력
 9 20  2 18 11
19  1 25  3 21
 8 24 10 17  7
15  4 16  5  6
12 13 22 23 14

출력
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9
'''

nums = []
for i in range(5):
    lists = list(map(int, input().split()))
    nums = nums + lists


def find_min(num):
    mins = 99
    next_num = []
    for k in range(len(num)):
        if num[k] < mins:
            mins = num[k]

    num[k] = num[0]
    num[0] = mins

    for k in range(1, len(num)):
        next_num.append(k)

    num = next_num
    return mins


result = [[0 for x in range(5)] for y in range(5)]

x_cnt = 0
y_cnt = 0



# 상 하 좌 우
def isWall(testX, testY, x, y, cnt):
    if testX >= 0 or (testX == 0 and testX <= 4):
        print('오른쪽')
        return x+1, y, cnt + 1

    elif testY >= 0 or (testY == 0 and testY <= 4):
        return x, y+1, cnt + 1

    elif not testX > 5 or (testX == 0 and testX >= 1):
        return x, y-1, cnt + 1

    elif not testY > 5 or (testY == 0 and testY <= 4):
        return x-1, y, cnt + 1



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = 0
y = 0


for k in range(25):
    result[x][y] = find_min(nums)
    cnt = 0
    for i in range(4):
        print(i)
        testX = x + dx[i]
        testY = y + dy[i]
        x, y, cnt = isWall(testX, testY, x, y, cnt)
        print(x, y)
        if cnt == 1:
            cnt = 0
            break

print(result)