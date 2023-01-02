def solution(food_times, k):
    sumFood_time = sum(food_times)
    if sumFood_time <= k:
        return -1

    L = len(food_times)
    hi = 100000000
    lo = 0

    while lo+1 < hi:
        mid = (hi+lo)//2
        time = mid * L
        for f in food_times:
            if f-mid < 0:
                time += f-mid

        if time < k:
            lo = mid
        else:
            hi = mid

    time = lo * L
    # time 초까지, lo 번 순회
    for i in range(L):
        food_times[i] -= lo
        if food_times[i] < 0:
            time += food_times[i]

    idx = 0
    for i in range(k-time):
        while food_times[idx] < 1:
            idx = (idx+1) % L
        food_times[idx] -= 1
        idx = (idx+1) % L

    while food_times[idx] < 1:
        idx = (idx+1) % L
    return idx+1
