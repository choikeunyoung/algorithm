from collections import deque

direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def BFS(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 0
    while queue:
        check = queue.popleft()
        for k in range(4):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            if (0 <= ny < N) and (0 <= nx < M):
                if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[check[0]][check[1]] + 1
                    queue.append((ny, nx))


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            BFS(i, j)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if matrix[i][j] == 1:
                print(-1, end=" ")
            else:
                print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()
