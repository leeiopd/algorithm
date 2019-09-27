def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while truck_weights:
        answer += 1
        for i in range(bridge_length):
            if bridge[i]:
                if i == 0:
                    bridge[i] = 0
                else:
                    bridge[i-1] = bridge[i]
                    bridge[i] = 0
        if sum(bridge)+truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge[-1] = truck

    return answer


bridge_length = int(input())
weight = int(input())
truck_weights = list(map(int, input().split()))
solution(bridge_length, weight, truck_weights)
