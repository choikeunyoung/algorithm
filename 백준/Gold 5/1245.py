from collections import deque
from pprint import pprint

direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def BFS(start):
    global cnt
    q = deque([start])
    if visited[start[0]][start[1]] == 0:
        visited[start[0]][start[1]] = matrix[start[0]][start[1]]
    while q:
        flag = 0
        check = q.popleft()
        for k in range(8):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                if matrix[ny][nx] < matrix[check[0]][check[1]]:
                    visited[ny][nx] = visited[check[0]][check[1]]
                elif matrix[ny][nx] == matrix[check[0]][check[1]]:
                    if not visited[ny][nx]:
                        visited[ny][nx] = visited[check[0]][check[1]]
                        q.append((ny,nx))
                    else:
                        if visited[ny][nx] < matrix[ny][nx]:
                            visited[ny][nx] = matrix[ny][nx]
                elif matrix[ny][nx] < visited[check[0]][check[1]]:
                    flag = 1
        if flag == 1:
            break
    else:
        cnt += 1




N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [0] * M for _ in range(N) ]

cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            BFS((i,j))
            pprint(visited)
            print(i,j,cnt)
print(cnt)