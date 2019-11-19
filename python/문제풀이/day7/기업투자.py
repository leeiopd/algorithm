import sys
sys.stdin  = open("기업투자.txt")
'''
어떤 투자가가 여러 기업들에게 돈을 투자해서 최대의 이익을 얻고자 한다.
단, 투자는 만원 단위로 할 수 있으며 각 기업은 많이 투자할수록 많은 이익을 투자가에게 돌려준다.
돈을 투자하지 않은 경우는 당연히 얻게 되는 이익도 없다. 예를 들어서,
한 투자가가 4만원을 갖고 두 개의 기업들에 각각 만원 단위로 투자했을 경우 얻을 수 있는 이익은 다음과 같다.
 

 
위의 경우 만일, 기업 A에 1만원, 기업 B에 3만원을 투자하는 경우 투자가가 얻는 이익은 14만원(5만원+9만원)이다.
4만원을 투자해서 가장 많은 이익을 얻을 경우 기업 B에만 4만원을 투자하는 경우로서 이때의 이익은 15만원이다. 여기서 투자가는 한 기업에 돈을 나누어 투자할 수는 없다.
 
투자액이 정해져 있고, 기업의 개수와 각 기업에 투자했을 경우에 얻게 되는 이익이 주어졌을 때 가장 많은 이익을 얻을 수 있는 이익금을 구하는 프로그램을 작성하라.


첫 줄은 투자 금액과 투자 가능한 기업들의 개수이며, 둘째 줄부터 각 줄은 투자액수 및 각 기업이 투자가에게 주는 이익이다.
단, 총 투자금액은 30만원을 넘지 않으며, 투자 가능한 기업의 개수는 최대 7개이다.

첫 줄에 얻을 수 있는 최대 이익을 출력한다.
'''
M, N = map(int, input().split())

invest_list = []
for m in range(M):
    invest_list.append(list(map(int, input().split())))


diff_list = [0] * N
result = 0

def diff_money(k=0):
    global investment, result
    if k == N:
        if sum(diff_list) == M:
            add = 0
            for i in range(N):
                if diff_list[i] != 0:
                    add += invest_list[diff_list[i]-1][i+1]
            if add > result:
                result = add

    else:
        for i in range(0, M+1):
            diff_list[k] = i
            diff_money(k+1)

diff_money()
print(result)


