'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서,

중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''
import sys

sys.stdin = open("02_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bus_info = list(map(int, input().split()))
    # info[0] = 연료, info[1] = 종점, info[2] = 충전기 설치 갯수
    charge_stop = list(map(int, input().split()))
    # charge_stop = 충전기 정류장 number

    # bus 출발 대기
    charge = bus_info[0]
    bus = 0
    charge_num = 0
    charge_stop_cnt = 0

    # bus 출발
    while not bus == bus_info[1] and not bus == -1:
        # charge & 정류장 check
        if charge == 0 and bus in charge_stop:
            charge = bus_info[0]
            charge_num += 1

        elif charge <= 0:
            # 버스 되돌리기
            while bus not in charge_stop:
                bus -= 1
                charge += 1
                # 지나친 충전 정류장 발견
                    # 무한루프 방지
                if charge_stop_cnt == bus:
                    bus = -2
                    break
                # 충전 후 다시 출발
                elif bus in charge_stop:
                    charge_stop_cnt = bus
                    charge = bus_info[0]
                    charge_num += 1
        # bus go
        bus += 1
        charge -= 1

    # 무한루프에 걸려 진행 불가시 '0'
    if  bus == -1:
        print(f'#{test_case} 0')

    # 마지막까지 도착시 결과 값
    else:
        print(f'#{test_case} {charge_num}')
