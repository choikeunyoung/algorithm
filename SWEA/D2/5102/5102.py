def BFS(start, target):
    queue = []
    for i in range(V):
        if matrix[start][i] == 1:
            queue.append(i)
    visited[start] = True
    node_cnt[start] = 0
    while queue:
        check = queue.pop(0)
        visited[check] = True
        for j in range(V):
            if matrix[check][j] == 1 and not visited[j]:
                node_cnt[j] = node_cnt[check] + 1
                if j == target:
                    return node_cnt[j]+1
                else:

                    queue.append(j)
                    
T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    matrix = [[0] * V for _ in range(V)]
    visited = [False] * V
    node_cnt = [0] * V
    for _ in range(E):
        A,B = map(int,input().split())
        matrix[A-1][B-1] = 1
        matrix[B-1][A-1] = 1

    S,G = map(int,input().split())

    ans = BFS(S-1,G-1)
    print(f"#{tc} {ans}")