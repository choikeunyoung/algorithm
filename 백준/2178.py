from collections import deque
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
visted_list = [[False] * M for _ in range(N)]
check = 0
dfs = deque([(0,0)])
while dfs:
    location = dfs.popleft()
    visted_list[location[0]][location[1]] = True
    for i in range(len(dx)):
        x = location[0] + dx[i]
        y = location[1] + dy[i]
        if (x >= 0 and y >= 0 ) and (x < N and y < M):
            if matrix[x][y] == 1 and visted_list[x][y] == False:
                dfs.append((x,y))
                matrix[x][y] = matrix[location[0]][location[1]] + 1
            if x == N-1 and y == M-1:
                print(matrix[x][y])
                check = 1
                break
    if check == 1:
        break