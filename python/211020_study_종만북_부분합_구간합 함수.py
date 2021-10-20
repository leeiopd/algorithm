scores = [100, 97, 86, 79, 66, 52, 49, 31]


def sum_a_to_b(scores, a, b):
    # 부분합 구하기
    return sum(scores[a:b+1]) // (b-a+1)


def partialSum(scores):
    # 부분합 array 구하기 최적화
    ret = [0] * len(scores)

    ret[0] = scores[0]
    for i in range(len(scores)):
        ret[i] = ret[i-1] + scores[i]
    # ret = [100, 197, 283, 362, 428, 480, 529, 602]
    return ret


def rangeSum(psum, a, b):
    # 부분합 array 가 주어질 때
    # a 부터 b 까지의 구간 합 구하기
    if(a == 0):
        return psum[b]

    return psum[b] - psum[a-1]
