'''
어느 나라에서 자국의 이익을 위해 스파이 조직을 만들어서 전 세계로 스파이를 침투 시켰다.

스파이들의 왕성한 활동으로 많은 이익이 발생하였는데 옆 나라가 이를 알고 스파이 조직을 알아내기 위해 조직도를 훔쳐내는데 성공했다.

그러나 조직도가 암호화 되어 있어서 이를 알아 볼 수가 없었다. 이제 당신이 조직도를 분석해내는 프로그램을 작성해야 한다.

편의상 스파이 이름은 숫자로 대체한다.

조직도는 보스<부하1><부하2> 형태로 보스의 부하는 최대 두 명이 될 수 있고 부하가 있는 경우 <부하<부하의부하1><부하의부하2>>안에 적혀있다.

부하가 없는 경우는 <>으로 표현된다.

예를 들어, 0<1<3<><>><4<7<><>><>>><2<5<><8<><>>><6<><>>> 로 되어 있는 조직도를 분석하면 아래와 같은 형태가 된다.

조직도를 분석하여 원하는 단계의 스파이들의 이름을 출력하는 프로그램을 작성하자.

첫 줄에 출력을 원하는 단계(N, 1≤N≤50)가 주어지고, 공백 한 칸 뒤에 조직도(S, 20,000자 이하)가 입력된다. 스파이 이름은 숫자이며 최대 4자리 임.

N단계에 맞는 조직원을 공백으로 구분하여 먼저 입력된 순서대로 출력한다.


'''

import sys

sys.stdin = open("C3_스파이.txt")

N, lists = map(str, input().split())

N = int(N)

mem = ''
new_list = []
for l in lists:
    if l.isdecimal():
        mem = mem + l
    elif mem:
        new_list.append(mem)
        new_list.append(l)
        mem = ''
    else:
        new_list.append(l)

nums = [[] for x in range(51)]
cnt = 0
for l in new_list:
    if l.isdecimal():
        nums[cnt].append(l)

    if l == '<':
        cnt += 1

    if l == '>':
        cnt -= 1

result = ''
for i in nums[N]:
    result = result + i + ' '

print(result)
