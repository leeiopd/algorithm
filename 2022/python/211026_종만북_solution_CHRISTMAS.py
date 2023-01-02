def wayToBuy(psum, k):
    # 한번으로 주문 가능한 방법
    # 1. [H, T] 구간의 합 = (psum[T] - psum[H-1])
    #
    # 2. 해당 구간의 합이 K명의 아이들에게 나눠줄 수 있는 경우
    #    (psum[T] - psum[H-1]) mod K = 0
    #    psum[T] mod K - psum[H-1] mod K = 0
    #    -> psum[T] mod K = psum[H-1] mod K
    #
    # 3. 나머지 연산 적용 후, psum[T] mod K = psum[H-1] mod K
    #    부분합 배열인 psum[i] = i 번까지의 부분합 % K 를 저장
    #    psum[0] = 0 으로 설정 ex) (Test Case) psum = [0 1 3 2 2 3 1]
    #
    # 4. 경우의 수 구하기 count[] 배열을 생성하여 psum[i] 의 개수 저장
    #    count[psum[i]] ++ ;  psum[0 1 3 2 2 3 1] -> count [1 2 2 2]
    #
    # 5. 전체 경우의 수는 count[] 의 각 경우에서, 2가지 경우를 뽑는 갯수를 구하는것
    #    res = sum ( count[i] C 2 ), count[i] > 1
    #
    #    (Test Case) count = [1 3 4 2] -> 3C2 + 4C2 + 2C2 = 3 + 6 + 1 = 10
    #    가령 psum[i] = 3 이 나오는 지점이 3개(=count[3]) 이라고 했을 때,
    #    구간을 선택하는 경우의 수는 [x, y], [x, z], [y, z] 로 3C2 이기 때문

    MOD = 20091101
    ret = 0
    count = [0] * k

    for i in range(len(psum)):
        count[psum[i]] += 1

    for i in range(k):
        if count[i] >= 2:
            ret += ((count[i] * (count[i] - 1)) // 2)
    return ret % MOD


def maxBuys(psum, k):
    # 주문이 겹치지 않게 최대 주문 경우의 수 / DP 이용
    # 1. DP[i] : 0 번 상자부터 i 번 상자까지 서로 겹치지 않고 구매할 수 있는 최대 수
    # 2. DP[i] = max( i 번째 상자를 선택하지 않은 경우, i 번째 상자를 선택하는 경우 )
    #          = max( DP[i-1], DP[ 최근에 psum 값이 같았던 index ] + 1)
    #          = max( DP[i-1], dp[prev[psum[i]]]+1 )
    #    % loc = prev[s] : 이전에 psum[] 값이 s 였던 마지막 위치

    dp = [0] * len(psum)
    prev = [-1] * k

    for i in range(len(psum)):
        loc = prev[psum[i]]
        if(loc != -1):
            # dp[i] 번째 상자를 사지 않은 경우의 수 vs i 이전에 psum 값이 같았던 경우의수 + 1
            dp[i] = max(dp[i-1], dp[loc]+1)

        # psum[i] 값의 마지막 위치를 현재로 갱신
        prev[psum[i]] = i

    return dp[-1]


T = int(input())


for _ in range(T):
    # N : 인형 상자의 개수
    # K : 어린이의 수
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    psum = [0] * (N+1)

    for i in range(1, N+1):
        psum[i] = (psum[i-1]+D[i-1]) % K

    orderOnce = wayToBuy(psum, K)
    orderMany = maxBuys(psum, K)

    print(orderOnce, orderMany)
