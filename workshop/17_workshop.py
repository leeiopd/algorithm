'''
퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.

우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.

교환전>



처음에는 첫번째 숫자판의 3과 마지막에 있는 8을 교환해서 8, 2, 8, 3, 8이 되었다.



다음으로, 두 번째 숫자판 2와 네 번째 숫자판의 8을 교환해서 8, 8, 8, 3, 2이 되었다.



정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.

숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.

여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.



94의 경우 2회 교환하게 되면 원래의 94가 된다.

정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

[입력]

가장 첫 줄은 전체 테스트 케이스의 수이다.

최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.

각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.

숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이다.

[출력]

각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.

같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.
'''
import sys
sys.stdin = open("17_input.txt")

T = int(input())

def game(cnt=0):
    global result

    point = int(''.join(map(str, nums)))
    if cnt == chance:
        result = max(result, point)
        return
    if point in mem:
        return
    mem.append(point)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            game(cnt + 1)
            nums[i], nums[j] = nums[j], nums[i]




for case in range(1, T + 1):
    nums, chance = input().split()
    number = int(nums)
    nums = list(map(int, nums))
    chance = int(chance)
    mem = []
    result = 0
    game()
    print('#{} {}'.format(case, result))
