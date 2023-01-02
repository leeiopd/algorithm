# direction  0:위 , 1:왼, 2:아래, 3:오 

def checkGrid(position, limit):
    if 0 <= position < limit:
        return position
    if position < 0:
        return limit-1
    if position == limit:
        return 0



def passFrame(y, x, D, H, W, grid):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    ldxy = [1, 0, 3, 2]
    rdxy = [3, 0, 1, 2]
    if grid[y][x] == 'S':
        return checkGrid(y+dy[D], H), checkGrid(x+dx[D], W), D
    elif grid[y][x] == 'L': 
        D = ldxy[D]
        return checkGrid(y+dy[D], H), checkGrid(x+dx[D], W), D
    else:
        D = rdxy[D]
        return checkGrid(y+dy[D], H), checkGrid(x+dx[D], W), D

def DFS(y, x, D, H, W, grid): 
    Y, X, DD = passFrame(y, x, D, H, W, grid)
    
    if path[y][x][DD]:
        return
        
    path[y][x][DD] += 1
    DFS(Y, X, DD, H, W, grid)
        

def solution(grid):
    global path
    MAX = 5
    path = [[[0 for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]
    answer = []

    H = len(grid)
    W = len(grid[0])

    for D in range(4):
        DFS(0, 0, D, H, W, grid)

    print(path)

    return path

solution(["R","R"])