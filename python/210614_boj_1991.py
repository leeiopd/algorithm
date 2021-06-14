N = int(input())
tree = {}

for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]


def preOrder(node):
    if node == '.':
        return

    print(node, end="")
    preOrder(tree[node][0])
    preOrder(tree[node][1])


def inOrder(node):
    if node == '.':
        return

    inOrder(tree[node][0])
    print(node, end="")
    inOrder(tree[node][1])


def postOrder(node):
    if node == '.':
        return

    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(node, end="")


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
