'''
삼성은행의 신입사원 정식이는 실수를 저질렀다.

은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.

하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며, 기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다.

예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.

정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.

정식이가 송금액을 추측하는 프로그램을 만들어주자.

( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )
'''
import sys

sys.stdin = open("15_input2.txt")

T = int(input())

def two_sum(two):
    two = two[::-1]
    add = 0
    for i in range(len(two)):
        add += int(two[i]) * (2**i)
    two_list.append(add)
    return

def three_sum(three):
    three = three[::-1]
    add = 0
    for i in range(len(three)):
        add += int(three[i]) * (3**i)
    three_list.append(add)
    return


for case in range(1, T+1):
    two = list(map(int, input()))
    three = list(map(int, input()))
    two_list = []
    three_list = []

    for i in range(len(two)):
        if two[i] == 1:
            two[i] = 0
            two_sum(two)
            two[i] = 1
        elif two[i] == 0:
            two[i] = 1
            two_sum(two)
            two[i] = 0

    for i in range(len(three)):
        if three[i] == 0:
            three[i] = 1
            three_sum(three)
            three[i] = 2
            three_sum(three)
            three[i] = 0
        elif three[i] == 1:
            three[i] = 0
            three_sum(three)
            three[i] = 2
            three_sum(three)
            three[i] = 1
        elif three[i] == 2:
            three[i] = 1
            three_sum(three)
            three[i] = 0
            three_sum(three)
            three[i] = 2

    result = list(set(two_list) & set(three_list))
    print(result[0])
