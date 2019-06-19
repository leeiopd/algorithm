'''
피보나치수열이란 앞의 두 수를 더하여 나오는 수열이다.
첫 번째 수와 두 번째 수는 1이고 세 번째 수는 첫 번째 수와 두 번째 수를 더하여 2가 된다. 피보나치수열을 나열해 보면 다음과 같다.

1, 1, 2, 3, 5, 8, 13...

자연수 N을 입력 받아 N번째 피보나치 수를 출력하는 프로그램을 작성하여라.

'''
import sys

sys.stdin = open("2_input.txt")



def fibo(N):
    global fibo_list

    fibo_list[0] = 1
    fibo_list[1] = 1

    if N <= 1:
        return fibo_list[N]
    else:
        cnt = 2
        while cnt < N:
            fibo_list[cnt] = fibo_list[cnt-1] + fibo_list[cnt-2]
            cnt += 1
        return fibo_list[N-1]

N = int(input())
fibo_list = [0] * 1000
result = fibo(N)

print(result)
