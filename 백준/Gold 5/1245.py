from collections import deque
from pprint import pprint

direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def BFS(start):
    global cnt
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        flag = 0
        check = q.popleft()
        for k in range(8):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                if matrix[ny][nx] > matrix[start[0]][start[1]]:
                    flag = 1
                    q = deque([])
                    break
                elif matrix[ny][nx] == matrix[start[0]][start[1]] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny,nx))
                else:
                    visited[ny][nx] = True
        if flag == 1:
            break
    else:
        cnt += 1




N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]

cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0 and not visited[i][j]:
            BFS((i,j))
            pprint(visited)
            print(i,j,cnt)
print(cnt)