from collections import deque
from pprint import pprint as print
N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
matrix_cnt = [[0]*N for _ in range(N)]


dx = [ -1, 0, 0, 1 ]
dy = [ 0, -1, 1, 0]

min_cnt = 0

stack = deque()

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0 and not visited[i][j]:
            matrix_cnt[i][j] = 1
            stack.append((i,j))
            while stack:
                index = stack.popleft()
                print(index)
                visited[index[0]][index[1]] = True
                for k in range(4):
                    x = dx[k] + index[1]
                    y = dy[k] + index[0]
                    if (x > 0 and y > 0) and (x < N and y < N):
                        if matrix[x][y] == 0 and not visited[x][y]:
                            stack.append((x,y))
                            matrix_cnt[x][y] = 1
        elif matrix[i][j] == 1:
            
print(matrix)
print(visited)
print(matrix_cnt)