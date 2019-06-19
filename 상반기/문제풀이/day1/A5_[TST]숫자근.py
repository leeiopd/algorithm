'''
각 자릿수를 계속 더하여 한 자리 숫자를 만드는 것을 숫자근(Digit Root)이라고 한다.
예를 들어 정수 65,536의 숫자근은 7이다, 그것은 6+5+5+3+6=25이고 이를 다시 2+5=7이기 때문이다.
 
n개의 정수가 입력되면 숫자근이 가장 큰 값을 찾는 프로그램을 작성하시오.



입력의 첫 줄에 정수의 개수 n(2≤n≤1,000)이 들어온다.
그 다음 줄부터 n개의 정수 m_i(1≤m_i≤1,000,000)가 한 줄에 한 개씩 들어온다.



숫자근이 가장 큰 정수를 출력한다. 단, 가장 큰 숫자근이 여러 개이면 그 중 가장 작은 수를 출력한다.
'''
import sys

sys.stdin = open("A5_input.txt")

N = int(input())

nums_list = []

def add_fun(num):
    while len(num) > 1:
        add = 0
        for n in num:
            i = int(n)
            add += i
        
        num = f'{add}'
    
    return num



for n in range(N):
    k = list(map(str, input().split()))
    if k[0] :
        nums_list.append(k[0])

result_add = 0
result_num = ''
for n in range(N):
    num = nums_list[n]
    res = int(add_fun(nums_list[n]))
    

    if res > result_add:
        result_add = res
        result_num = num
    if res == result_add:
        int_num = int(num)
        int_result_num = int(result_num)
        if int_num < int_result_num:
            result_num = num
            

print(result_num)