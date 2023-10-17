import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def DFS(start):
    global cnt
    visited[start] = cnt
    martix[start].sort()
    for i in martix[start]:
        if visited[i] == -1:
            cnt += 1
            DFS(i)

N, M, R = map(int,input().split())
martix = [ [] for _ in range(N+1) ]
visited = [-1] * (N+1)

for _ in range(M):
    A, B = map(int,input().split())
    martix[A].append(B)
    martix[B].append(A)

cnt = 1
DFS(R)
for k in range(1,N+1):
    if visited[k] == -1:
        print(0)
    else:
        print(visited[k])