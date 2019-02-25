'''
돼지는 먹이를 좋아한다.
돼지가 하루에 2번을 먹는 것은 너무 적고 10번은 너무 많아서 좋아하지 않는다.
돼지는 먹는 양이 달라서 하루에 3번만 먹어도 만족하는 놈이 있고 8번을 먹어도 만족하지 못하는 놈이 있다.
하루에 최소 4번은 먹어야 만족하는 돼지는 5번, 6번을 먹어도 물론 만족하지만 3번은 만족하지 못한다.
이제 먹이를 주는 횟수에 따른 돼지의 만족 또는 불만족을 알 때, 하루에 최소 먹이횟수를 찾아라.
먹이의 횟수는 3에서 9사이이다.
4
4 N
7 Y
5 N
6 Y

'''
import sys

sys.stdin = open("A3_input.txt")

N = int(input())

if N == 0:
    print('F')
else:
    result = 10
    time_list = []
    for n in range(N):
        t_list = list(map(str, input().split()))
        time_list.append(t_list)
        
    for t in time_list:
        time = int(t[0])
        if t[1] == 'Y' and time < result :
            result = time
            
    for t in time_list:
        time = int(t[0])
        if t[1] == 'N':
            if result <= time:
                result = 'F'
        
    print(result)