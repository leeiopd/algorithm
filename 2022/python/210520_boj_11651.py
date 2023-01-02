import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))
    
for point in sorted(points, key=lambda x: (x[1], x[0])):
    print(point[0], point[1])