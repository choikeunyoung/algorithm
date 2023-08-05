T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    
    dx_cross = [-1, 1, 1, -1]
    dy_cross = [-1, -1, 1, 1]
    
    max_value = 0
    
    for i in range(N):
        for j in range(N):
            value = 0
            plus_cnt = matrix[i][j]
            multi_cnt = matrix[i][j]
            for k in range(1,M):
                for l in range(4):
                    x = j + dx[l]*k
                    y = i + dy[l]*k
                    x_cross = j + dx_cross[l]*k
                    y_cross = i + dy_cross[l]*k
                    if (0 <= x < N) and (0 <= y < N):
                        plus_cnt += matrix[y][x]

                    if (0 <= x_cross < N) and (0 <= y_cross < N):
                        multi_cnt += matrix[y_cross][x_cross]

            value = max(plus_cnt, multi_cnt)
            if max_value < value:
                max_value = value
    print(f"#{tc} {max_value}")