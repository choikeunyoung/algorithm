# N = input()

# N = str(int(N) + 1)
# N_length = len(N)
# ans = ""
# if len(N) % 2 == 0:
#     if N[:N_length//2] == N[N_length:N_length//2-1:-1]:
#         print(N)
#     else:
#         ans = N[:N_length//2] + N[:N_length//2][::-1]
#         if int(ans) >= int(N):
#             print(ans)
#         else:
#             if N[N_length//2] == "9":
#                 N = str(int(N) + 10**(N_length//2))
#                 if len(N) > N_length:
#                     N = N[:N_length//2+1] + N[:N_length//2][::-1]
#                     print(N)
#                 else:
#                     print(N[:N_length//2]+N[:N_length//2][::-1])
#             else:
#                 ans = str(int(ans) + 10**(N_length//2))
#                 print(ans[:N_length//2]+ans[:N_length//2][::-1])
# else:
#     if N[:N_length//2] == N[N_length//2+1:N_length//2-1:-1]:
#         print(N)
#     else:
#         ans = N[:N_length//2+1] + N[:N_length//2][::-1]
#         if int(ans) >= int(N):
#             print(ans)
#         else:
#             if N[N_length//2] == "9":
#                 N = str(int(N) + 10**(N_length//2))
#                 if len(N) > N_length:
#                     N = N[:N_length//2] + N[:N_length//2][::-1]
#                     print(N)
#                 else:
#                     print(N[:N_length//2+1]+N[:N_length//2][::-1])
#             else:
#                 print(int(ans) + 10**(N_length//2))

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS():
    global cnt
    while q:
        a = q.popleft()
        for k in range(4):
            ny = a[0]+dy[k]
            nx = a[1]+dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1 and  visited[ny][nx] == -1:
                    visited[ny][nx]  = visited[a[0]][a[1]] +1
                    now = ny,nx
                    q.append(now)


N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
visited = [[-1]*(M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            visited[i][j] = 0
            q = deque()
            start = i,j
            q.append(start)
            BFS()
for i in range(N):
    print(*visited[i])