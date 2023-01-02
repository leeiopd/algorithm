import sys

C = int(input())


def getPartialMatch(S, L):
    pi = [0] * L

    begin = 1
    matched = 0

    while begin + matched < L:
        if S[begin + matched] == S[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
            else:
                begin += 1
    return pi


for _ in range(C):
    S = sys.stdin.readline()
    L = len(S)
    pi = getPartialMatch(S, L)

    Sr = S[::-1]

    begin = 0
    matched = 0

    while begin < L:
        if matched < L and S[begin + matched] == Sr[matched]:
            matched += 1

            if begin + matched == L:
                print(L * 2 - matched)
                break
        else:
            if matched:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
            else:
                begin += 1
