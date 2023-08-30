def DFS(start, check):
    if check > cnt[-1]:
        cnt[-1] = check
    for k in range(4):
        ny = start[0] + dy[k]
        nx = start[1] + dx[k]
        if ( 0 <= ny < N ) and ( 0 <= nx < N ):
            if (matrix[start[0]][start[1]] + 1 == matrix[ny][nx]) and not visited[ny][nx]:
                visited[ny][nx] = True
                DFS((ny,nx),check+1)
                visited[ny][nx] = False


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    visited = [ [False] * N for _ in range(N) ]
    ans = []
    for i in range(N):
        for j in range(N):
            cnt = [matrix[i][j], 0]
            DFS((i,j), 1)
            ans.append(cnt)
    check = 0
    answer = 0
    ans.sort()
    for l in ans:
        if check < l[-1]:
            answer = l[0]
            check = l[-1]
    print(f"#{tc} {answer} {check}")