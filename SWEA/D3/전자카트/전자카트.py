def DFS(start, total, check):
    global min_value
    if check == N-1:
        min_value = min(min_value, matrix[start][0] + total)
        return
    else:
        for k in range(N):
            if not visited[k] and start != k:
                visited[start] = True
                DFS(k, total+matrix[start][k], check+1)
                visited[k] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    min_value = 10**4
    visited = [False] * N
    DFS(0, 0, 0)
    print(f"#{tc} {min_value}")