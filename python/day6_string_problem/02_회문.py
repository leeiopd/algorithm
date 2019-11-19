'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.


G O F F A K W F S M

O Y E C R S L D L Q

U J A J Q V S Y Y C

J A E Z N N Z E A J

W J A K C G S G C F

Q K U D G A T D Q L

O K G P F P Y R K Q

T D C X B M Q T I O

U N A D R P N E T Z

Z A T W D E K D Q F


[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import sys

sys.stdin = open("02_input.txt")

T = int(input())

def x_check(M,N,map):
    for y in range(N):
        for start_x in range(N-M+1):
            check = ''
            for x in range(start_x, start_x+M):
                check = check + map[y][x]
            if check == check[::-1]:
                return check
    return 0

def y_check(M, N, map):
    for x in range(N):
        for start_y in range(N-M+1):
            check = ''
            for y in range(start_y, start_y+M):
                check = check + map[y][x]
            if check == check[::-1]:
                return check
    return 0

for case in range(1, T+1):
    N, M= input().split()
    N = int(N) # map 크기
    M = int(M) # 회문 길이
    map = []

    for i in range(N):
        string = list(input())
        map.append(string)
    if x_check(M, N, map):
        result = x_check(M, N, map)
    elif y_check(M, N, map):
        result = y_check(M, N, map)
    print(f'#{case} {result}')





