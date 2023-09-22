def DFS(start):
    visited[start] = True
    for i in range(1,N+1):
        if matrix[start][i] == 1 and not visited[i]:
            DFS(i)

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    visited = [False] * (N+1)
    matrix = [ [0] * (N+1) for _ in range(N+1) ]
    for _ in range(M):
        A, B = map(int,input().split())
        matrix[A][B] = 1
        matrix[B][A] = 1
    cnt = 0
    for i in range(1,N+1):
        if not visited[i]:
            DFS(i)
            cnt += 1
    print(f"#{tc} {cnt}")