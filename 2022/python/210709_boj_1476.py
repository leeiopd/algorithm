# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
# 1 1 1 -> 1
# 1년이 지날 때마다, 세 수는 모두 1씩 증가한다.
# 15 -> 15 15 15
# 16 -> 1 15 15

ESM = list(map(int, input().split()))

check = [1, 1, 1]
cnt = 1

while True:
    if check == ESM:
        print(cnt)
        break

    check[0] = (check[0] + 1) % 16
    if not check[0]:
        check[0] = 1

    check[1] = (check[1] + 1) % 29
    if not check[1]:
        check[1] = 1

    check[2] = (check[2] + 1) % 20
    if not check[2]:
        check[2] = 1

    cnt += 1
