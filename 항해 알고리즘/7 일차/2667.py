from collections import deque

def BFS(start):
    global cnt
    queue = deque([start])
    visited[start[0]][start[1]] = True
    check = 0
    while queue:
        next = queue.popleft()
        for k in range(4):
            ny = next[0] + direction[k][0]
            nx = next[1] + direction[k][1]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False and matrix[ny][nx] == 1:
                    queue.append((ny,nx))
                    visited[ny][nx] = True
        check += 1
    cnt += 1
    answer.append(check)



N = int(input())

matrix = []
direction = [(-1,0),(0,1),(1,0),(0,-1)]
answer = []
cnt = 0

for _ in range(N):
    matrix.append(list(map(int,input())))

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == False:
            BFS((i,j))

answer.sort()
print(cnt)

for ans in answer:
    print(ans)