import sys

N = int(sys.stdin.readline())

points = []

for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))
    
for point in sorted(points):
    print(point[0], point[1])