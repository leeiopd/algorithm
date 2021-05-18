N = int(input())

cards = [0] + list(map(int, input().split()))
# index = card 개수
# cards[index] = card 가격
# N 개 샀을때, 가장 카드 가격이 높은 수

dp = [0] + [0] * N
dp[1] = cards[1]

for i in range(1, N+1):
    tmp = [cards[i]]
    for j in range(1, i+1):
        print(j, i-j)
        tmp.append(cards[j] + dp[i-j])
    dp[i] = max(tmp)
    
print(dp[N])