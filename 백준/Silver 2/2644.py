import sys

input = sys.stdin.readline

def DFS(start):
    visited[start] = 1
    global cnt
    for i in range(N):
        if matrix[start][i] == 1:
            if visited[i] == 0:
                if i == end:
                    ans.append(cnt)
                    print(cnt)
                    return
                else:
                    cnt += 1
                    visited[i] = visited[start] + 1
                    DFS(i)
                    visited[i] = 0
                    cnt -= 1

N = int(input())
start, end = map(int,input().split())
m = int(input())
matrix = [ [0]*(N+1) for _ in range(N+1) ]
visited = [0] * (N+1)
for _ in range(m):
    A,B = map(int,input().split())
    matrix[A][B] = 1
    matrix[B][A] = 1
cnt = 1
ans = []
DFS(start)
print(ans)