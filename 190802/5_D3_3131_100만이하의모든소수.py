'''
1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

[입력]

이 문제의 입력은 없다.

[출력]

1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.
'''
nums = [2, 3, 5, 7]

for i in range(10, 1000001):
    flag = True
    k = int(i ** 0.5)
    for j in range(2, k+1):
        if i % j == 0:
            flag = False
            break
    if flag == False:
        continue
    else:
        nums.append(i)
result = ' '.join(map(str, nums))
print(result)

# 에라토스테네스의 체
