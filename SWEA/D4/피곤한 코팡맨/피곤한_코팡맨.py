def DFS(pos, cnt , max_value, min_value):
    global min_ans
    if (max_value - min_value) > min_ans:
        return
    if cnt == k_cnt:
        if (max_value - min_value) < min_ans:
            min_ans = max_value - min_value
        return
    else:
        for k in range(8):
            next_max_value = max_value
            next_min_value = min_value
            ny = pos[0] + dy[k]
            nx = pos[1] + dx[k]
            if ( 0 <= ny < N ) and ( 0 <= nx < N ):
                # if not visited[ny][nx]:
                    if next_max_value < matrix_index[ny][nx]:
                        next_max_value = matrix_index[ny][nx]
                    if next_min_value > matrix_index[ny][nx]:
                        next_min_value = matrix_index[ny][nx]
                    # visited[ny][nx] = True
                    if matrix[ny][nx] == "K":
                        DFS((ny,nx), cnt+1, next_max_value, next_min_value)
                    else:
                        DFS((ny,nx), cnt, next_max_value, next_min_value)
                    # visited[ny][nx] = False
                    
N = int(input())
matrix = [ list(map(str,input())) for _ in range(N) ]
matrix_index = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [False]*N for _ in range(N) ]
min_ans = 10**7
dx = [-1, 0, 1, -1, 1, -1, 0 ,1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
k_cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == "K":
            k_cnt += 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == "P":
            min_value = matrix_index[i][j]
            max_value = matrix_index[i][j]
            visited[i][j] = True
            DFS((i,j), 0, matrix_index[i][j], matrix_index[i][j])
print(min_ans)  