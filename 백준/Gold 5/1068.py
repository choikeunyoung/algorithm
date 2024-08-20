from collections import deque

def BFS(start):
    global cnt
    global target
    visited = [False] * N
    visited[start] = True
    q = deque([start])
    while q:
        next = q.popleft()
        if graph[next]:
            for i in graph[next]:
                if not visited[i] and i != target:
                    q.append(i)
                    visited[i] = True
        else:
            cnt += 1

N = int(input())

graph = [ [] for _ in range(N)]

num_list = list(map(int,input().split()))

target = int(input())
start = 0
for i in range(N):
    if i != target:
        if num_list[i] != -1:
            graph[num_list[i]].append(i)
    if num_list[i] == -1:
        start = i
cnt = 0

if start != target:
    BFS(start)

print(cnt)