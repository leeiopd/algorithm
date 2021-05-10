'''
10개의 정수를 입력받아 부분집합의 합이 0이 되는것이 몇개가 존재하는지를
계산하는 함수를 작성해 보자.
'''

arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
# arr = list(map(int, input().split()))

cnt = 0
for i in range(1, 1 << n):
    lists = []
    add = 0
    for j in range(n):
        if i & (1<<j):
            add += arr[j]

    if add == 0:
        cnt+=1
print(cnt)

