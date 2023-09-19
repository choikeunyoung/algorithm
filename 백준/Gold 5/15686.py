from collections import deque

one_pos = []
two_pos = []

N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            one_pos.append((i,j))
        elif matrix[i][j] == 2:
            two_pos.append((i,j))

min_value = 10**6
print(two_pos, one_pos)
for i in one_pos:
    total = 10**6
    for j in two_pos:
        total = min(total,((i[0]-j[0])**2+(i[1]-j[1])**2))
    if min_value > total:
        min_value = total
print(min_value)