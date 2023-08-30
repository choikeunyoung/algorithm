def DFS(start, total):
    global min_value
    visited[start[0]][start[1]] = True
    if total > min_value:
        return
    if start == (N-1, N-1):
        if total < min_value:
            min_value = total
        return
    else:
        for i in range(2):
            ny = start[0] + dy[i]
            nx = start[1] + dx[i]
            if ( 0 <= ny < N ) and ( 0 <= nx < N ):
                if not visited[ny][nx]:
                    DFS((ny,nx),total+matrix[ny][nx])
                    visited[ny][nx] = False
                    
T = int(input())

dx = [1, 0]
dy = [0, 1]

for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    visited = [ [False] * N for _ in range(N) ]
    min_value = 10**4
    DFS((0,0),matrix[0][0])
    print(f"#{tc} {min_value}")