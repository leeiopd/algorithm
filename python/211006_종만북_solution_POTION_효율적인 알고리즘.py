# 효율적인 알고리즘
# r_list 들의 약수를 찾아 해결

# 1. 모든 재료 중 가장 많이 들어간 재료 찾기
#     -> X = max( p_list[i] / r_list[i] ), 모든 재료는 X 배 이상 들어야가한다.
# 2. r_list[i] * X 는 항상 정수
#     -> X <= Y = ( a / b ), Y 는 X 이상의 유리수
# 3. r_list[i] * Y 가 정수인 최소 Y 찾기
#      -> r_list[i] * Y = r_list[i] * ( a / b ), b 는 모든 r_list 수들의 약수가 되어야함

# 최적화
#      -> p_list[i] / r_list[i] 의 최대값 X 를 구하고 b 를 곱하여 a 를 얻는게 아니라
#         max( p_list[i] * b / r_list[i] ) 를 직접 구하여 분수연산을 회피

c = int(input())


def get_gcd(a, b):
    return get_gcd(b, a % b) if b else a


def ceil(a, b):
    # 분수 a/b 보다 같거나 큰 최소의 자연수
    return (a + b - 1) // b


def solve(r_list, p_list, n):
    # r_list 의 모든 수들의 최대 공약수 구하기
    b = r_list[0]
    for i in range(1, n):
        b = get_gcd(b, r_list[i])

    # 최소 b/b = 1 배 이므로, a 의 초기값을 b 로 설정
    a = b

    # X 를 직접 구하는 대신 ceil(p_list[i] * b, r_list[i]) 의 최대값을 구하기
    for i in range(n):
        a = max(a, ceil(p_list[i] * b, r_list[i]))

    res = [0] * n
    for i in range(n):
        res[i] = (r_list[i] * a // b) - p_list[i]
    return res


for _ in range(c):
    n = int(input())

    # 필요한 재료 양
    r_list = list(map(int, input().split()))

    # 넣은 양
    p_list = list(map(int, input().split()))

    answer = solve(r_list, p_list, n)

    print(" ".join(map(str, answer)))
