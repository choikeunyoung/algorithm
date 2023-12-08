def DFS(start):
    stack = [start]
    global cnt
    global max_width
    visited[start[0]][start[1]] = True
    width = 1
    while stack:
        check = stack.pop()
        for k in range(4):
            dx = direction[k][1] + check[1]
            dy = direction[k][0] + check[0]
            if 0 <= dx < M and 0 <= dy < N:
                # 방문하지 않고 matrix 값이 1인 경우
                if not visited[dy][dx] and matrix[dy][dx] == 1:
                    # stack에 좌표값 추가
                    stack.append((dy, dx))
                    # 방문처리
                    visited[dy][dx] = True
                    # 넓이 체크
                    width += 1
    # 반복문이 다 끝났을 경우 최대 너비 갱신
    if max_width < width:
        max_width = width
    # DFS를 실행한 횟수 체크
    cnt += 1


N, M = map(int, input().split())
# 방향배열
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 인풋값
matrix = [list(map(int, input().split())) for _ in range(N)]
# 방문처리
visited = [[False] * M for _ in range(N)]
# 섬의 개수
cnt = 0
# 최대넓이
max_width = 0

for i in range(N):
    for j in range(M):
        # 방문하지 않았고 섬인경우 DFS 실행
        if not visited[i][j] and matrix[i][j] == 1:
            DFS((i, j))

print(cnt)
print(max_width)
