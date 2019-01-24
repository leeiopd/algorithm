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
import pprint

nums = []
for i in range(5):
    lists = list(map(int, input().split()))
    nums = nums + lists


def find_min(nums):
    mins = 99

    for k in range(len(nums)):
        if nums[k] < mins:
            mins = nums[k]
            index = k

    nums[index] = nums[0]

    nums = nums[1:]
    return mins, nums


result = [[0 for x in range(5)] for y in range(5)]

x_cnt = 0
y_cnt = 0



# 상 하 좌 우
def isWall(x, y, result, cnt):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    if cnt == 'u':
        k = 0
    elif cnt == 'd':
        k = 1
    elif cnt == 'l':
        k = 2
    elif cnt == 'r':
        k = 3

    testX = x + dx[k]
    testY = y + dy[k]


    # cnt == 방향 // ------좌표 범위 조건------//------- 빈칸인지 확인-------//
    if cnt =='r' and testX >= 0 and testX < 5 and result[testY][testX] == 0:
        return testX, testY, cnt
    # cnt == 방향 // 가려는 방향이 범위를 넘어가거나 빈칸이 아니라면, 다음 방향 체크 (빈칸이거나 가려는 방향이 채워져 있는지) -> 방향 변경
    elif cnt == 'r' and (result[testY+1][testX-1] == 0 or result[testY][testX] != 0 ):
        cnt='d'
        return testX-1, testY+1, cnt

    if cnt == 'd' and testY >= 0 and testY < 5 and result[testY][testX] == 0:
        return testX, testY, cnt
    elif cnt == 'd' and (result[testY-1][testX-1] == 0 or result[testY][testX] != 0):
        cnt='l'
        return testX-1, testY-1, cnt

    if cnt == 'l' and testX >= 0 and testX < 5 and result[testY][testX] == 0:
        return testX, testY, cnt
    elif cnt == 'l' and  ( result[testY-1][testX+1] == 0 or result[testY][testX] != 0):
        cnt='u'
        return testX+1, testY-1, cnt

    if cnt == 'u' and testY >= 0 and testY < 5 and result[testY][testX] == 0:
        return testX, testY, cnt
    elif cnt == 'u' and (result[testY+1][testX+1] == 0 or result[testY][testX] != 0):
        cnt='r'
        return testX+1, testY+1, cnt

x = 0
y = 0
cnt = 'r'
for k in range(25):
    result[y][x], nums = find_min(nums)
    x, y, cnt = isWall(x, y, result, cnt)

pprint.pprint(result)