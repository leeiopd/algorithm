N, K = map(int, input().split())

queue = [ i for i in range(1, N+1)]
result = []
idx = 0
while queue:
    idx = (idx+(K-1)) % len(queue)
    result.append(queue.pop(idx))
    
    
print("<"+", ".join(map(str, result))+">")