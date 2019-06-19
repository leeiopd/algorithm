T = 10

for case in range(1, T+1):
    long  = int(input())
    maps = []
    for y in range(8):
        nums = list(input())
        maps.append(nums)
    
    cnt = 0
    for y in range(8):
        for start_x in range(8):
            tmp = []
            for x in range(start_x, 8):
                tmp.append(maps[y][x])
            if tmp == tmp[::-1]:
                if cnt < len(tmp):
                    cnt = len(tmp)
    for x in range(8):
        for start_y in range(8):
            tmp = []
            for y in range(start_y, 8):
                tmp.append(maps[y][x])
            if tmp == tmp[::-1]:
                if cnt < len(tmp):
                    cnt = len(tmp)
    print(cnt)