N = int(input())
matrix = [ list(map(str,input())) for _ in range(N) ]
matrix_index = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [False]*N for _ in range(N) ]

dx = [-1, 0, 1, -1, 1, -1, 0 ,1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == "P":
            min_value = matrix_index[i][j]
            max_value = matrix_index[i][j]
            visited[i][j] = True
            n_i = i
            n_j = j
            queue = [(i,j)]
            while queue:
                print(queue)
                check = queue.pop(0)
                check_value = []
                check_index = []
                for k in range(8):
                    ny = check[0] + dy[k]
                    nx = check[1] + dx[k]
                    if ( 0 <= ny < N ) and ( 0 <= nx < N ):
                        if not visited[ny][nx]:
                            if matrix[ny][nx] == "K":
                                visited[ny][nx] = True
                                queue.append((ny,nx))
                                break
                            else:
                                check_value.append(matrix_index[ny][nx])
                                check_index.append((ny,nx))
                if check_value:
                    check_mid = min(check_value)
                    check_pos = check_value.index(check_mid)
                    visited[check_index[check_pos][0]][check_index[check_pos][1]] = True
                    queue.append((check_index[check_pos][0],check_index[check_pos][1]))
                    if min_value > check_mid:
                        min_value = check_mid

                    if max_value < check_mid:
                        max_value = check_mid
print(min_value,max_value)
