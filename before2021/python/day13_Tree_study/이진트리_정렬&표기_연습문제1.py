'''
정점의 개수 : 13
1 ~ 13개
'''

N = 13

long = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
nums = []
for n in range(0, N+1):
    k = [0, 0, 0]           #left right perent
    nums.append(k)

long = list(map(int, long.split()))

for i in range(len(long)//2):
    a = long[i*2]
    b = long[i*2 + 1]

    if nums[a][0] == 0:
        nums[a][0] = b
    elif nums[a][1] == 0:
        nums[a][1] = b
    nums[b][2] = a

def postorder(node):
    if node != 0:
        postorder(nums[node][0])
        postorder(nums[node][1])
        print(node, end=" ")

def preorder(node):
    if node != 0:
        print(node, end=" ")
        preorder(nums[node][0])
        preorder(nums[node][1])

def inorder(node):
    if node != 0:
        inorder(nums[node][0])
        print(node, end=" ")
        inorder(nums[node][1])

print("전위순회 :", end='')
preorder(1)
print()
print("중위순회 :", end='')
inorder(1)
print()
print("후위순회 :", end='')
postorder(1)


