'''
8명의 사람들이 아래 그림과 같이 원형으로 앉아서 폭탄 돌리기 게임을 한다. 폭탄은 작은 번호의 사람부터 큰 번호의 사람으로 이동한다.

맨 처음에는 K번 사람이 폭탄을 갖고 있다.

 
폭탄을 가진 사람은 퀴즈를 풀게 되는데 퀴즈를 맞힐 때에만 폭탄을 다음 사람에게 넘겨줄 수 있다.

퀴즈를 틀리거나 통과하게 되면 그 사람이 다음 문제를 풀어야 한다. 폭탄은 210초와 211초 사이에 터지게 된다.

이 때 폭탄이 터질 때 폭탄을 갖고 있던 사람을 구하여라.

단, 모든 퀴즈가 다 진행된 후에도 210초가 지나지 않았으면 가장 마지막에 폭탄을 가진 사람에게서 폭탄이 터지게 된다.



첫 번째 줄에는 처음 폭탄을 가진 사람의 번호 K가 주어진다. (1 ≤ K ≤ 8)
두 번째 줄에는 게임이 진행되는 동안 공개된 퀴즈의 수 N이 주어진다. (1 ≤ N ≤ 100)
세 번째 줄부터 N개의 줄에는 퀴즈를 풀거나 통과를 결정할 때까지 걸린 시간 T (1 ≤ T ≤ 100)와 정답 여부 Z가 주어진다.
Z가 'T'이면 퀴즈를 맞았다는 것을 의미하고, 'F'이면 틀렸다는 것을, 'P'이면 통과했다는 것을 의미한다.


폭탄이 터질 때 폭탄을 갖고 있던 사람의 번호를 출력한다.

1
5
20 T
50 T
80 T
50 T
30 T
'''

import sys

sys.stdin = open("A_input.txt")

K = int(input()) # 폭탄을 가진 사람 번호 1~8
N = int(input()) # 공개된 퀴즈의 수'

bomb_time = 210

for n in range(N):
    T, Z = input().split()
    T = int(T)
    if Z == 'T':
        if bomb_time - T > 0:
            K = (K+1) % 8
            bomb_time -= T
        else:
            result = K
            break
    elif Z == 'F':
        if bomb_time - T > 0:
            bomb_time -= T
        else:
            result = K
            break
    elif Z == 'P':
        if bomb_time - T > 0:
            bomb_time -= T
        else:
            result = K
            break
result = K
if result == 0:
    result = 8
print(result)
    