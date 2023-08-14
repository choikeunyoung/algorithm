T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                visited[i][j] = True
                stack = []
                for k in range(4):
                    x = j + dx[k]
                    y = i + dy[k]
                    if (0 <= x < N) and (0 <= y < N):
                        if matrix[y][x] == 0:
                            stack.append([y,x])
                            while stack:
                                check = stack.pop()
                                if not visited[check[0]][check[1]]:
                                    visited[check[0]][check[1]] = True    n = int(input())
# fb = [0]*(11)
# fb[0] = [1, 0]
# fb[1] = [0, 1]
# fb[2] = [1, 1]

# for i in range(3, 11):
#     fb[i] = [fb[i-1][0] + fb[i-2][0], fb[i-1][1] + fb[i-2][1]]
# print(*fb[10])