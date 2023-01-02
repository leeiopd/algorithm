# 유클리드 알고리즘 (Euclidean algorithm)
# p, q (p > q) 의 공약수의 집합 == p-q, q 의 공약수 집합
# gcd(p, q) == gcd(p-q, q)
#
# gcd(6, 15) = gcd(9, 6) = gcd(3, 6) = gcd(3, 3) = gcd(3, 0)


def get_gcd(p, q):
    if p < q:
        p, q = q, p

    if q == 0:
        return p

    return get_gcd(p-q, q)


gcd = get_gcd(6, 15)
print(gcd)
# 3
