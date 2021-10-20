# A[] 의 제곱의 부분 합 백터 sqpsum, A[] 의 부분 합 벡터 psqum이 주어질 때
# A[a, b] 의 분산을 반환한다.

def variance(sqpsum, psum, a, b,):

    # 해당 구간의 평균 계산
    mean = sum(psum[a:b+1]) / (b-a+1)

    # 분산 계산
    ret = sum(sqpsum[a:b+1]) - (2 * mean *
                                sum(psum[a:b-1])) + ((b-a+1) * mean * mean)

    return ret / (b-a+1)
