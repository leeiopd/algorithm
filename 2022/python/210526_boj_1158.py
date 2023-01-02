N, K = map(int, input().split())

queue = [ i for i in range(1, N+1)]
result = "<"
while queue:
    for _ in range(K):
        queue.append(queue.pop(0))
    result = result+str(queue.pop(0))+", "
    
result = result[:-2]+">"

print(result)