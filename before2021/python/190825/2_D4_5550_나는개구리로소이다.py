''''
개구리 한 마리가 한번 울면 “croak”하는 소리가 난다. 개구리 한 마리가 계속 여러 번 울면 울음소리가 다음처럼 나타날 수 있다.

“croakcroak”, “croak”, “croakcroakcroakcroak”

영은이는 개구리를 연구하기 위해 많은 개구리를 사육한다. 영은이는 개구리들을 키우는 우리에 들어와 울음소리를 녹음했다.

여러 개구리가 동시에 울면 울음소리가 섞여서 녹음된다.

이 때 한 개구리의 울음소리는 녹음된 울음소리에서 부분 문자열로 나타난다. 이 부분 문자열은 연속하지 않아도 된다. 예를 들어 "crcoarkcoroakak"와 같을 수 있다.

그렇다면, 녹음을 할 때 있었던 개구리는 최소 몇 마리일까?


[입력]

첫 번째 줄에 테스트 케이스의 수가 주어진다.

각 테스트 케이스의 첫 번째 줄에 개구리들의 울음소리를 나타내는 길이 5 이상 2,500이하인 문자열이 주어진다. 이 문자열은 ‘c’, ‘r’, ‘o’, ‘a’, ‘k’로만 이루어져 있다.

[출력]

각 테스트 케이스마다 첫번째 줄에는 ‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, 개구리의 최소 수를 출력한다.

개구리의 울음소리로 불가능한 경우 -1을 출력하면 된다.

'''
import sys
sys.stdin = open('5550.txt')

T = int(input())

for case in range(1, T+1):
    croaks = input()

    checks = []
    fail = 0
    for croak in croaks:

        # 울음소리 시작
        if croak == 'c':
            flag = 1

            # 이전 개구리 check
            for i in range(len(checks)):
                # 다 울은 개구리가 존재 한다면
                if checks[i] == 0:
                    flag = 0
                    checks[i] += 4
                    break
            # 다 울은 개구리가 존재 하지 않으면 개구리 추가
            if flag:
                checks.append(4)

        # 울음소리 r
        elif croak == 'r':
            flag = 1
            for i in range(len(checks)):
                # c 울음소리 낸 개구리 존재
                if checks[i] == 4:
                    flag = 0
                    checks[i] -= 1
                    break
            # 이전 울음소리가 없었는데 울었으니 fail
            if flag:
                fail = 1

        # 울음소리 o
        elif croak == 'o':
            flag = 1
            for i in range(len(checks)):
                # r 울음소리를 낸 개구리 존재
                if checks[i] == 3:
                    flag = 0
                    checks[i] -= 1
                    break
            # 이전 울음소리가 없었는데 울었으니 fail
            if flag:
                fail = 1

        # 울음소리 a
        elif croak == 'a':
            flag = 1
            for i in range(len(checks)):
                # o 울음소리를 낸 개구리 존재
                if checks[i] == 2:
                    flag = 0
                    checks[i] -= 1
                    break
            # 이전 울음소리가 없었는데 울었으니 fail
            if flag:
                fail = 1

        # 울음소리 k
        elif croak == 'k':
            flag = 1
            for i in range(len(checks)):
                # a 울음소리를 낸 개구리 존재
                if checks[i] == 1:
                    flag = 0
                    checks[i] -= 1
                    break
            # 이전 울음소리가 없었는데 울었으니 fail
            if flag:
                fail = 1

    # fail이면 결과는 -1
    if fail:
        print('#{} {}'.format(case, -1))
    else:
        # 모든 개구리가 다 울음을 완료 했으면
        if sum(checks) == 0:
            # 개구리 마리수
            result = len(checks)
            print('#{} {}'.format(case, result))
        # 모든 개구리가 울음을 완료 안했으면 -1
        else:
            print('#{} {}'.format(case, -1))
