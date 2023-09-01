from collections import deque

def BFS(start):
    queue = deque(start)
    while queue:
        
        
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    visited = [ [0]*M for _ in range(N) ]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "L":
                