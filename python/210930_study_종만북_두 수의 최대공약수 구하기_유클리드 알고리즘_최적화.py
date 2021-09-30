# 유클리드 알고리즘 (Euclidean algorithm)
# p, q (p > q) 의 공약수의 집합 == p-q, q 의 공약수 집합
# gcd(p, q) == gcd(p-q, q)
#
# gcd(6, 15) = gcd(9, 6) = gcd(3, 6) = gcd(3, 3) = gcd(3, 0)

# gcd(1024, 6) = gcd(1018, 6) = gcd(1012, 6) = .... = gcd(4, 6) = gcd(4, 2) = gcd(2, 2) = gcd(2, 0)
# 하나하나 빼는 것 보다, 나눠서 나머지를 취하자


def get_gcd_new(p, q):
    if q == 0:
        return p

    return get_gcd_new(q, p % q)


gcd = get_gcd_new(1024, 6)
print(gcd)
# 2
