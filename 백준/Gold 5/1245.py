from collections import deque

direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def BFS(start):
    global cnt
    for k in range(8):
        ny = start[0] + direction[k][0]
        nx = start[1] + direction[k][1]
        if ( 0 <= ny < N ) and ( 0 <= nx < M ):
            if matrix[ny][nx] > matrix[start[0]][start[1]]:
                break
            
    else:
        cnt += 1

N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
# visited = [ [-1] * M for _ in range(N) ]

cnt = 0
for i in range(N):
    for j in range(M):
        BFS((i,j))
print(cnt)