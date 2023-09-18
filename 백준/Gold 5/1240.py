import sys
from collections import deque

input = sys.stdin.readline

def DFS(start,end):
    global check
    if start == end:
        check = answer[:]
        return
    else:
        stack = graph[start]
        for i in stack:
            if not visited[i]:
                visited[i] = True
                answer.append(i)
                DFS(i,end)
                answer.pop()
                visited[i] = False



distance_dict = {}

max_num = 0
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B, dis = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
    if max_num < max(A,B):
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
    ans = 0
    visited = [False] * (max_num+1)
    X, Y = map(int,input().split())
    visited[X] = True
    answer = [X]
    check = 0
    DFS(X,Y)
    check_length = len(check)
    for i in range(check_length-1):
        ans += distance_dict[check[i]][check[i+1]]
    print(ans)