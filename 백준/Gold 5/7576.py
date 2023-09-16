from collections import deque


def BFS():
    # 요일 체크하는 변수
    global day
    # matrix 좌표가 1인 값을 저장한 리스트 q
    while q:
        # q에서 값을 하나씩 빼주면서
        check = q.popleft()
        # 방향배열 탐색
        for k in range(4):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            # 범위내 있을 경우
            if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                # matrix 값이 0 이고 visited 값이 0 인 경우
                if matrix[ny][nx] == 0 and visited[ny][nx] == 0:
                    # visited[ny][nx] 에 이전값 + 1 진행
                    visited[ny][nx] = visited[check[0]][check[1]] + 1
                    # matrix 에 1 처리
                    matrix[ny][nx] = 1
                    # visited 값이 day 값보다 큰 경우 갱신
                    if visited[ny][nx] > day:
                        day = visited[ny][nx]
                    # q에 값 추가
                    q.append((ny,nx))


M, N = map(int,input().split())
# 방향배열
direction = [(0,-1), (-1,0), (0,1), (1,0)]
# 매트리스 생성
matrix = [ list(map(int,input().split())) for _ in range(N)]
# 방문처리 리스트
visited =  [ [0] * M for _ in range(N) ]
# 몇일지나면 다 익는지 체크
day = 0
q = deque()
# 1의 좌표값들을 리스트에 저장
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            visited[i][j] = 1
            q.append((i,j))
# 함수 실행
BFS()
# 반복문 탈출 조건 변수
flag = 0
# 만약 matrix 에 0 인 값이 있는 경우
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            # 반복문 탈출
            flag = 1
            break
    if flag == 1:
        break
# 반복문이 탈출되지 않았으면
if flag == 0:
    # day 가 0인 경우 모두 익어있으므로 day 출력
    if day == 0:
        print(day)
    # 외의 경우 day - 1 출력
    else:
        print(day-1)
# 반복문이 탈출된 경우 -1 출력
else:
    print(-1)