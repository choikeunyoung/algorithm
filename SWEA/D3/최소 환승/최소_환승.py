def BFS(start, end):
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        check = queue.pop(0)
        if check != T:
            for i in arr[check]:
                if i != T and visited[i] == 0:
                    visited[i] = visited[check] + 1
                    queue.append(i)
        elif check == end:
            return visited

N, M = map(int,input().split())

arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    A, B = map(int,input().split())
    arr[A].append(B)
    arr[B].append(A)
T = int(input())

BFS(1,N)
if visited[N] == 0:
    print(-1)
else:
    print(visited[N]-1)