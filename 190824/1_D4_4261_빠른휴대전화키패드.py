'''
동한이는 창고에서 오래된 애니콜 휴대전화를 발견했다.

이 휴대전화의 키패드는 아래와 같이 생겼다.



이 키패드는 각 키를 여러 번 눌러 영문을 입력할 수 있는데, a를 입력하려면 2를 한 번, b를 입력하려면 2를 두 번 누르는 식이다.

그러나 동한이는 이 방식이 너무 느리다고 생각하여 문자열을 빠르게 타이핑할 수 있도록 키패드를 다음과 같이 바꿔 보려고 한다.

사용할 단어들을 미리 휴대폰에 저장한 뒤, 해당 알파벳이 써있는 숫자를 한 번씩만 누르면 가능한 여러 단어 중에 사전에 저장된 단어를 찾아서 입력하는 것이다.

예를 들면 car를 입력하려면 222, 2, 777을 입력하는 것이 정상이지만 이 자판의 경우 227을 입력하면 aap, aaq, …, ccs 등 3×3×4=36개의 단어 중에 사전에 존재하는 단어를 출력해준다.

하지만 동한이는 이 시스템의 문제점을 발견하였다. 이 예시의 경우 car는 cap과 표현이 겹친다는 점을 확인할 수 있는데,

이처럼 키 입력이 동일한 단어가 여럿 존재할 수 있다는 것이다.

동한이는 얼마나 이런 경우가 자주 발생되는지 확인하기 위해, 사전과 키 입력이 주어지면 해당하는 키 입력과 대응되는 단어가 몇 개인지 구하는 프로그램을 원한다.

이러한 프로그램을 작성하라.


[입력]

맨 위 줄에 테스트 케이스의 개수가 주어진다.

각 테스트 케이스마다 순서대로 첫 번째 줄에 키 입력을 뜻하는 2에서 9까지의 자연수로 이루어진 1 이상 1000 이하 길이의 문자열 S와

단어의 개수 N(1 ≤ N ≤ 1000)이 주어진다.

그 다음 줄에 N개의 단어(모든 단어의 길이들의 합은 1000000 이하)가 띄어쓰기로 구분되어 주어진다.


[출력]

각 테스트 케이스마다 키 입력에 대응되는 사전 안의 단어의 수를 출력하라.


[Hint]

첫 번째 케이스에서 "mono"가 숫자 6에 대응되는 유일한 단어이다.

두 번째 케이스에서 두 단어의 첫째 글자는 숫자 5에, 둘째 글자는 숫자 2에 모두 해당된다.
'''
import sys
sys.stdin = open('4261.txt')

T = int(input())

for case in range(1, T+1):
    S, N = map(str, input().split())
    words = list(map(str, input().split()))

    # 버튼 정리
    keys = {'a':'2', 'b':'2','c':'2','d':'3' ,'e':'3','f':'3', 'g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6', 'o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
    cnt = 0
    for word in words:
        flag = 1
        # 알파벳의 버튼과 입력 버튼을 순서대로 비교
        for w in range(len(word)):
            # 알파벳의 버튼과 입력버튼이 다를때
            if keys[word[w]] != S[w]:
                # flag로 다름을 분기
                flag = 0
                break
        # 모든 단어의 알파벳과 입력버튼이 순서대로 같을 때
        if flag:
            cnt += 1
    print('#{} {}'.format(case, cnt))