from collections import deque

direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited_dict = {}
use = []

for i in range(N):
    for j in range(N):
        visited_dict[matrix[i][j]] = 1

total_length = len(visited_dict.keys())

for i in visited_dict.keys():
    visited = [[False] * N for _ in range(N)]
    for k in range(N):
        for l in range(N):
            if matrix[k][l] <= i:
                visited[k][l] = True
    
    for k in range(N):
