def BFS(start,end):
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        check = queue.pop(0)
        for i in matrix[check]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[check] + 1
                
    return visited[end] - 1
    
T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    matrix = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        A,B = map(int,input().split())
        matrix[A].append(B)
        matrix[B].append(A)


    S,G = map(int,input().split())
    ans = BFS(S,G)
    if ans < 0:
        ans = 0
    print(f"#{tc} {ans}")
