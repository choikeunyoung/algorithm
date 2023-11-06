from collections import deque

direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

use = []
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS((i, j))
