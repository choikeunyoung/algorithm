from collections import deque

def BFS(start):
    q = deque([start])
    visited[start] = 1
    while q:
        check = q.popleft()
        for i in range(N):
            if matrix[check][i] == 1 and visited[i] == 0:
                visited[i] = visited[check] + 1
                q.append(i)

N = int(input())
M = int(input())

matrix = [ [0] * (N+1) for _ in range(N+1) ]
visited = [0] * (N+1)
for _ in range(M):
    A,B = map(int,input().split())
    matrix[A][B] = 1
    matrix[B][A] = 1
    
    
start = int(input())
BFS(start)
cnt = 0
for i in range(N+1):
    if i != start:
        if visited[i] > 1:
            cnt += 1
print(cnt)