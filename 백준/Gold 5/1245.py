from collections import deque
from pprint import pprint
# 8방향 탐색
direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def BFS(start):
    # 봉우리 체크할 변수
    global check_tree
    q = deque([start])
    # 시작지점 방문처리
    visited[start[0]][start[1]] = True
    while q:
        check = q.popleft()
        # 방향 탐색
        for k in range(8):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                # 주위에 큰 봉우리가 있는경우 봉우리 아니라는 체크
                if matrix[ny][nx] > matrix[check[0]][check[1]]:
                    check_tree = False
                # 방문하지 않았고 값이 같은 봉우리가 있으면 방문처리 후 q에 추가
                if not visited[ny][nx] and matrix[ny][nx] == matrix[check[0]][check[1]]:
                    visited[ny][nx] = True
                    q.append((ny,nx))

N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [0] * M for _ in range(N) ]

cnt = 0
for i in range(N):
    for j in range(M):
        # 방문하지 않으면 함수 실행
        if not visited[i][j]:
            # 초기값 봉우리 True 선언
            check_tree = True
            BFS((i,j))
            # 만약 봉우리가 true 라면 cnt 증가
            if check_tree:
                cnt += 1
print(cnt)