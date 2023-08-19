import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 깊이 우선 탐색 함수
def DFS(start):
    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = True
    # stack 에 i, j 튜플 형태로 들어온 값 추출
    while stack:
        col, row = stack.pop()
        # 들어온 값들의 방향배열을 탐색함
        for k in range(4):
            x = row + dx[k]
            y = col + dy[k]
            # M, N 사이에 존재하며 방문하지 않고 1인 경우
            if (0 <= x < M) and (0 <= y < N):
                if not visited[y][x] and matrix[y][x] == 1:
                    # 방문 처리후 스택에 값 추가
                    visited[y][x] = True
                    stack.append((y,x))

T = int(input())

for tc in range(T):
    M, N, K = map(int,input().split())
    matrix = [ [0] * M for _ in range(N) ]
    visited = [ [False] * M for _ in range(N) ]
    cnt = 0
    # input 값을 k 번 받아오며 그래프에 1 추가
    for _ in range(K):
        A, B = map(int,input().split())
        matrix[B][A] = 1

    for i in range(N):
        for j in range(M):
            # matrix i, j 가 1이고 방문하지 않았을 경우
            if matrix[i][j] == 1 and not visited[i][j]:
                # DFS 함수 호출
                DFS((i,j))
                # 끝나면 cnt 증가
                cnt += 1

    print(cnt)