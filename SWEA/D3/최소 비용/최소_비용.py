from collections import deque

direction = [(0,-1), (-1,0), (0,1), (1,0)]


def BFS():
    q = deque([(0,0)])
    visited[0][0] = 1
    while q:
        check = q.popleft()
        for k in range(4):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            if ( 0 <= ny < N ) and ( 0 <= nx < N ):
                fuel = 1
                if matrix[ny][nx] > matrix[check[0]][check[1]]:
                    fuel += matrix[ny][nx] - matrix[check[0]][check[1]]
                if visited[ny][nx] > (visited[check[0]][check[1]] + fuel):
                    visited[ny][nx] = visited[check[0]][check[1]] + fuel
                    q.append((ny,nx))
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    visited = [ [10**6]*N for _ in range(N) ]
    BFS()
    print(f"#{tc} {visited[N-1][N-1]-1}")