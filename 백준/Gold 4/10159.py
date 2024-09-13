import sys

input = sys.stdin.readline

def DFS(start):
    global N
    cnt = 1
    visited = [False] * (N+1)
    stack = [start]
    visited[start] = True
    while stack:
        next = stack.pop()
        for nextPos in range(1,N+1):
            if graph[next][nextPos] == 1 and not visited[nextPos]:
                visited[nextPos] = True
                cnt += 1
                stack.append(nextPos)
    return cnt

N = int(input())

M = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    S,E = map(int,input().split())
    graph[S][E] = 1
    graph[E][S] = -1
print(graph)

for i in range(1,N+1):
    print(DFS(i))