import sys
sys.stdin = open("상자포장하기.txt")
'''
A, B라는 두 사람은 상자를 포장하려 한다.
다음 조건에 따라 A와 B는 상자를 포장하고 포장한 상자를 모두 더한 합을 구한다.
1] A는 큰 상자에서 작은 상자 순서로 포장을 하고, B는 작은 상자에서 큰 상자 순서로 포장을 한다. 
2] 입력된 상자 크기의 순서는 바뀔 수 없다.
3] A, B가 같은 상자를 사용할 수 없다.
4] 사용되지 않는 상자가 있을 수 있다.

예를 들어 상자 크기가 3 10 5 2 8 100 4 3 과 같이 주어진다면 A는 "10 4 3" B는 "3 5 8 100" 순서로 포장을 한다.
A와 B가 포장한 상자들을 모두 더한 결과의 최대합을 구한다. 
결과는 A의 합 (10+4+3) = 17, B의 합(3+5+8+100) = 116 이므로 17+116 = 133이 된다. 

첫 줄에 testcase 수가 입력된다.
두 번째 줄에 사용할 수 있는 상자의 크기 목록의 개수 N이 입력된다. (1<=N<=20) 
세 번째 줄에 상자 크기의 목록이 공백으로 구분되어 입력된다.
상자의 크기는 최소 1, 최대 1000의 범위를 갖는다. 

A,B 가 포장한 상자의 크기 합의 최대가 출력된다.
'''
T = int(input())

def check_box_A(A_list, box):
    if A_list:
        if A_list[-1] > box:
            return True
        else:
            return False
    else:
        return True

def check_box_B(B_list, box):
    if B_list:
        if B_list[-1] < box:
            return True
        else:
            return False
    else:
        return True



def boxing(k, A, B):
    global result, A_list, B_list

    if k == N:
        add = sum(A_list) + sum(B_list)
        if add > result:
            result = add

    else:
        set_list[k] = 0
        boxing(k+1, A, B)

        if check_box_A(A_list, box[k]):
            set_list[k] = 1
            A_list.append(box[k])
            boxing(k+1, A+box[k], B)
            A_list.pop()
        if check_box_B(B_list, box[k]):
            set_list[k] = 2
            B_list.append(box[k])
            boxing(k + 1, A, B+box[k])
            B_list.pop()


for case in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    set_list = [0] * N
    result = 0
    A_list = []
    B_list = []
    boxing(0, 0, 0)
    print(result)