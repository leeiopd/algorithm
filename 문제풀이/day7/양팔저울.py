import sys
sys.stdin = open("양팔저울.txt")
'''
양팔 저울과 몇 개의 추가 주어졌을 때, 이를 이용하여 입력으로 주어진 구슬의 무게를 확인할 수 있는지를 결정하려고 한다.
무게가 각각 1g과 4g인 두 개의 추가 있을 경우, 주어진 구슬과 1g 추 하나를 양팔 저울의 양쪽에 각각 올려놓아 수평을 이루면 구슬의 무게는 1g이다.
또 다른 구슬이 4g인지를 확인하려면 1g 추 대신 4g 추를 올려놓으면 된다.
구슬이 3g인 경우 아래 <그림 1>과 같이 구슬과 추를 올려놓으면 양팔 저울이 수평을 이루게 된다.
따라서 각각 1g과 4g인 추가 하나씩 있을 경우 주어진 구슬이 3g인지도 확인해 볼 수 있다.

<그림 2>와 같은 방법을 사용하면 구슬이 5g인지도 확인할 수 있다. 구슬이 2g이면 주어진 추를 가지고는 확인할 수 없다.
 
추들의 무게와 확인할 구슬들의 무게가 입력되었을 때, 주어진 추만을 사용하여 구슬의 무게를 확인 할 수 있는지를 결정하는 프로그램을 작성하시오.

첫째 줄에는 추의 개수가 자연수로 주어진다. 추의 개 수는 12 이하이다.
둘째 줄에는 추의 무게들이 자연수로 가벼운 것부터 차례로 주어진다. 같은 무게의 추가 여러 개 있을 수도 있다.
추의 무게는 500g이하이며, 입력되는 무게들 사이에는 빈칸이 하나씩 있다. 세 번째 줄에는 무게를 확인하고자 하는 구슬들의 개수가 주어진다.
확인할 구슬의 개수는 7이하이다. 네 번째 줄에는 확인하고자 하는 구슬들의 무게 Gi( 0 <= Gi <=40000)가 정수로 주어지며,  입력되는 무게들 사이에는 빈 칸이 하나씩 있다.

주어진 각 구슬의 무게에 대하여 확인이 가능하면 Y, 아니면 N을 차례로 출력한다. 한 개의 줄로 이루어지며, 각 구슬에 대한 답 사이에는 빈칸을 하나씩 둔다.
'''
N = int(input())
nums = list(map(int, input().split()))
B = int(input())
balls = list(map(int, input().split()))

def check(k, left, right):
    global nums, result
    if result == "Y":
        return
    if right > left:
        return
    add = right
    for i in range(k, N):
        add += nums[i]
    if add < left:
        return

    if k == N:
        if sum(set_list) == 0:
            return
        r_add = 0
        l_add = ball
        for i in range(N):
            if set_list[i] == 1:
                l_add += nums[i]
            if set_list[i] == 2:
                r_add += nums[i]
        if r_add == l_add:
            result = "Y"
        return

    else:
        set_list[k] = 1
        check(k + 1, left + nums[k], right)
        if result == "Y":
            return
        set_list[k] = 2
        check(k + 1, left, right + nums[k])
        if result == "Y":
            return
        set_list[k] = 0
        check(k + 1, left, right)
        if result == "Y":
            return



for case in range(B):
    ball = balls[case]
    result = "N"
    if ball in nums:
        result = "Y"
    else:
        set_list= [0] * N
        check(0, ball, 0)
    print(result)