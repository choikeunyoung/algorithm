from collections import deque
from pprint import pprint

direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def BFS(start):
    global check_tree
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        check = q.popleft()
        for k in range(8):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                if matrix[ny][nx] > matrix[check[0]][check[1]]:
                    check_tree = False
                
                if not visited[ny][nx] and matrix[ny][nx] == matrix[check[0]][check[1]]:
                    visited[ny][nx] = True
                    q.append((ny,nx))




N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [0] * M for _ in range(N) ]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            check_tree = True
            BFS((i,j))
            if check_tree:
                cnt += 1
print(cnt)