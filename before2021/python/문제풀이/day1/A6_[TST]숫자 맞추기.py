'''
경곽이는 친구들과 게임을 하기로 했다. 이 게임에는 n명의 플레이어가 참가한다.
게임의 룰은 다음과 같다.
각각의 플레이어는 1이상 100이하의 좋아하는 정수를 카드에 적어서 제출한다.
각 플레이어는 자신과 같은 수를 쓴 사람이 없을 경우에, 자신이 카드에 쓴 만큼의 점수를 얻는다.
자신과 같은 수를 쓴 사람이 있는 경우에는 득점할 수 없다.
경곽이와 친구들은 게임을 3번 했다. 각 플레이어가 3번 게임에 대해서 쓴 카드의 정수가 주어질 때,
각 플레이어가 3번 게임에서 얻는 점수의 합계를 구하는 프로그램을 작성하시오.


첫 번째 줄에는 정수 n(2 <= n <= 200)이 주어진다.
두 번째 줄부터 n줄에 걸쳐서 각각 3개의 1이상 100이하의 자연수가 공백으로 구분되어 입력된다.

'''
import sys

sys.stdin = open("A6_input.txt")


N = int(input())

cards = []

for n in range(N):
    cards.append(list(map(int, input().split())))

score = [0] * N

for game in range(3):
    for people in range(N):
        p_card = cards[people][game]
        cnt = 0
        for player in range(N):
            if p_card == cards[player][game]  and people != player :
                cnt += 1
                break
        if cnt == 0:
            score[people] += p_card

for c in score:
    print(c)