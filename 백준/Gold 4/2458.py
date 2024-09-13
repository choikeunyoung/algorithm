import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[10**9] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
    
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
    
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[j][i] != 10**9 or graph[i][j] != 10**9:
            continue
        else:
            break
    else:
        answer += 1
print(answer)