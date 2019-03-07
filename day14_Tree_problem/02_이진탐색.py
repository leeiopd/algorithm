import sys

sys.stdin = open("02_input.txt")

T = int(input())

def inorder(node):
    global in_list
    if node != 0:
        inorder(tree[node][0])
        in_list.append(node)
        inorder(tree[node][1])

for case in range(1, T+1):
    N = int(input())
    tree = [[0, 0, 0] for x in range(1001)]

    for i in range(1, N+1):
        if i*2 > N:
            break
        tree[i][0] = 2 * i
        if i*2 +1 >N:
            break
        tree[i][1] = 2 * i + 1

    in_list = []

    inorder(1)

    for i in range(1, N+1):
        k = i - 1
        if in_list[k] == N//2:
            node = i

        if in_list[k] == 1:
            top = i
    print(f'#{case} {top} {node}')