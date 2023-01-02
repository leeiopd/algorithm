import sys

T = int(sys.stdin.readline())
    
for _ in range(T):
    N = int(sys.stdin.readline())
    stickers = []
    answer = 0
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]
    
    for i in range(2, N):
        stickers[0][i] += max(stickers[0][i-2], stickers[1][i-1])
        stickers[1][i] += max(stickers[1][i-2], stickers[0][i-1])
    print(stickers)
    print(max(stickers[0][N-1], stickers[1][N-1]))
    print()

# import copy


# T = int(sys.stdin.readline())

# def deleteStiker(i, j, stickers):
#     stickers[i][j] = 0
#     if i:
#         stickers[i-1][j] = 0
#     else:
#         stickers[i+1][j] = 0
#     if j < len(stickers[0]) - 1:
#         stickers[i][j+1] = 0
#     if j > 0:
#         stickers[i][j-1] = 0
#     return stickers
    
# def DFS(i, j, stickers, res):
#     global answer
#     if sum(stickers[0]) == 0 and sum(stickers[1]) == 0:
#         answer = max(answer, res)
#         return
    
#     for i in range(2):
#         for j in range(N):
#             if stickers[i][j]:
#                 tmp = stickers[i][j]
#                 stikersCopy = deleteStiker(i, j, copy.deepcopy(stickers))
#                 DFS(i, j, stikersCopy, res+tmp)
            
    
# for _ in range(T):
#     N = int(sys.stdin.readline())
#     stickers = []
#     answer = 0
#     for _ in range(2):
#         stickers.append(list(map(int, sys.stdin.readline().split())))
    
#     for i in range(2):
#         for j in range(N):
#             stickersCopy = deleteStiker(i, j, copy.deepcopy(stickers))
#             DFS(i, j, stickersCopy, stickers[i][j])
#     print(answer)