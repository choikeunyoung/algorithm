import sys

input = sys.stdin.readline
# 방향 탐색
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# DFS
def DFS(start):
    stack = [start]
    # 시작값 방문처리
    visited[start[0]][start[1]] = True
    while stack:
        check = stack.pop()
        # 방향배열 탐색
        for k in range(8):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            # 범위 내에 존재
            if ( 0 <= ny < h ) and ( 0 <= nx < w ):
                # 방문하지 않았고 matrix 값이 1인 경우
                if not visited[ny][nx] and matrix[ny][nx] == 1:
                    # 방문 처리 후 stack에 값 추가
                    visited[ny][nx] = True
                    stack.append((ny,nx))

while True:
    # w, h 가 0, 0 인경우까지 반복문 시행
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    # 지도 생성
    matrix = [ list(map(int,input().split())) for _ in range(h) ]
    # 방문 처리
    visited = [ [False] * w for _ in range(h) ]
    # 섬의 갯수 체크
    cnt = 0
    for i in range(h):
        for j in range(w):
            # matrix 값이 1이고 방문하지 않았으면
            if matrix[i][j] == 1 and not visited[i][j]:
                # DFS 시행 후 cnt 증가
                DFS((i,j))
                cnt += 1
    print(cnt)