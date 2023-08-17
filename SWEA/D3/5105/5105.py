T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    flag = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                queue = [(i, j)]
                while queue:
                    check = queue.pop(0)
                    for k in range(4):
                        x = check[1] + dx[k]
                        y = check[0] + dy[k]
                        if (0 <= x < N) and (0 <= y < N):
                            if not visited[y][x] and matrix[y][x] != 1:
                                cnt += 1
                                queue.append((y,x))
                                visited[y][x] = True
                                distance[y][x] = distance[y-dy[k]][x-dx[k]] + 1
                                if matrix[y][x] == 3:
                                    print(f"#{tc} {distance[y][x]-1}")
                                    flag = 1
                                    break
                    if flag == 1:
                        break
                else:
                    print(f"#{tc} 0")
            if flag == 1:
                break
        if flag == 1:
            break
