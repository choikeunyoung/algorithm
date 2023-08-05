N, M = map(int,input().split())

K = int(input())

matrix = [ list(map(str,input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# "@" 폭탄
# "#" 벽
# "_" 빈칸

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "@":
            matrix[i][j] = "%"
            for k in range(4):
                for l in range(1,K+1):
                    x = j + dx[k]*l
                    y = i + dy[k]*l
                    if (0 <= x < M) and (0 <= y < N):
                        if matrix[y][x] == "#":
                            break
                        elif matrix[y][x] == "_":
                            matrix[y][x] = "%"

for mat in matrix:
    for j in mat:
        print(j,end="")
    print()