import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    global max_num
    for i in graph[start]:
        visited = [0]*(max_num+1)
        visited[start] = distance_dict[i][start]
        visited[i] = distance_dict[start][i]
        total = distance_dict[start][i]
        q = deque(graph[i])
        while q:
            check = q.popleft()
            if check == Y:
                visited[check] = total + distance_dict[check]
                return visited[check]


distance_dict = {}

max_num = 0
graph = [[] for _ in range(N+1)]
N, M = map(int,input().split())
for _ in range(N-1):
    A, B, dis = map(int,input().split())
    graph[A].append(B)
    if max_num > max(A,B):
        max_num = max(A,B)
    if A in distance_dict:
        distance_dict[A][B] = dis
    else:
        distance_dict[A] = [0]*1001
        distance_dict[A][B] = dis
    
    if B in distance_dict:
        distance_dict[B][A] = dis
    else:
        distance_dict[B] = [0]*1001
        distance_dict[B][A] = dis

for _ in range(M):
    X, Y = map(int,input().split())
    answer = 0
    BFS(X)