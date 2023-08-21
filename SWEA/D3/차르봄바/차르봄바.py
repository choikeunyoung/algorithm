T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for tc in range(1, T+1):
    N, P = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_virius = 0
    for i in range(N):
        for j in range(N):
            current_virius = matrix[i][j]
            for k in range(1,P+1):
                for l in range(4):
                    y = i + dy[l]*k
                    x = j + dx[l]*k
                    if ( 0 <= x < N ) and ( 0 <= y < N ):
                        current_virius += matrix[y][x]

            if max_virius < current_virius:
                max_virius = current_virius
    print(f"#{tc} {max_virius}")