
def enQ(n):
    global last
    
    last += 1
    c = last
    p = c//2
    Q[last] = n
    while c>1 and Q[p] > Q[c] :
        Q[p], Q[c] = Q[c], Q[p]
        c = p
        p = p//2
        
def deQ():
    global last
    r = Q[1]
    Q[1] = Q[last]
    last -= 1
    p = 1
    
    while p < last:
        c1 = p*2
        c2 = p*2 + 1
        
        if c2 <= last: # 양쪽 자식 다 있는 경우
            if Q[c1] < Q[c2] : c = c1
            else: c = c2
            if Q[c] < Q[p]: # 둘중 작은쪽 부모 비교
                Q[c], Q[p] = Q[p], Q[c]
            else: break
            
        elif c1 <= last: # 왼쪽 자식만 있는 경우
            if Q[c1] < Q[p]: # 부모와 비교
                Q[c1], Q[p] = Q[p], Q[c1]
                p = c1
            else: break
        else: break
    return r
                