from collections import deque
# 방향 배열
direction = [(0,-1), (-1,0), (0,1), (1,0)]
# BFS 함수
def BFS():
    # 탐색할 수 있는 갯수
    global zero_cnt
    # 최소값
    global min_value
    # 무한루프 시행
    while True:
        # 한 범위 탐색 후 탐색할 수 있는 범위 체크하는 리스트
        middle_jihoon = []
        middle_fire = []
        # 불의 범위가 존재할 경우
        while fire:
            # popleft통해서 앞에서부터 값을 뺴줌
            check = fire.popleft()
            # 방향배열 탐색
            for k in range(4):
                ny = check[0] + direction[k][0]
                nx = check[1] + direction[k][1]
                # ny, nx 값이 범위내에 있을 경우
                if ( 0 <= ny < R ) and ( 0 <= nx < C ):
                    # visited 값이 0 이면 불표시 -2 해줌
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = -2
                        # 중간에 불의 위치를 저장할 리스트에 저장
                        middle_fire.append((ny,nx))
                        # . 이였던 공간이 줄었으므로 -1
                        zero_cnt -= 1
        # 지훈이의 위치값이 빠질때까지 반복
        while jihoon:
            check = jihoon.popleft()
            # 방향배열 탐색
            for k in range(4):
                ny = check[0] + direction[k][0]
                nx = check[1] + direction[k][1]
                # 범위내에 있으면
                if ( 0 <= ny < R ) and ( 0 <= nx < C ):
                    # 방문처리가 안된 경우
                    if visited[ny][nx] == 0:
                        # 이전값에 +1 을 해줌
                        visited[ny][nx] = visited[check[0]][check[1]] + 1
                        # 지훈이의 중간위치 저장
                        middle_jihoon.append((ny,nx))
                        # . 공간이 없어지므로 가능한 공간 -1
                        zero_cnt -= 1
                        # 만약 끝에 도달한 경우
                        if ny == 0 or ny == R-1 or nx == 0 or nx == C-1:
                            # 최소값 갱신
                            if visited[ny][nx] < min_value:
                                min_value = visited[ny][nx]
        # 지훈이가 갈 공간이 없으면 탈출
        if not middle_jihoon:
            return
        # 움직일 수 있는 공간이 없으면 탈출
        if zero_cnt <= 0:
            return
        # 불에 중간에 저장한 위치 추가
        fire.extend(middle_fire)
        # 지훈이리스트에 중간에 저장한 리스트 추가
        jihoon.extend(middle_jihoon)


R,C = map(int,input().split())
# 좌표 받아옴
matrix = [ list(map(str,input())) for _ in range(R) ]
# 방문 체크
visited = [ [0] * C for _ in range(R) ]
# 불과 지훈이 위치 체크
fire = deque([])
jihoon = deque([])
# 이동 가능한 공간
zero_cnt = 0
# 최소값
min_value = 10**9
for i in range(R):
    for j in range(C):
        # 지훈이 위치가 끝인 경우 바로 종료
        if matrix[i][j] == "J":
            if i == 0 or i == R-1:
                print(1)
                exit()
            if j == 0 or j == C-1:
                print(1)
                exit()
            visited[i][j] = 1
            jihoon.append((i,j))
        # 불의 위치 체크
        elif matrix[i][j] == "F":
            fire.append((i,j))
            # 불의 위치 -2 대입
            visited[i][j] = -2
        # 벽의 경우 -1 넣어줌
        elif matrix[i][j] == "#":
            visited[i][j] = -1
        # 외의 경우 이동 가능한 공간 체크
        else:
            zero_cnt += 1
BFS()
# BFS 탐색이 끝났을때 이동 가능한 공간이 있고 min_value 가 초기값이 아니면 min_value 추가
if zero_cnt >= 0 and min_value != 10**9:
    print(min_value)
# 외의 경우 불가능한 경우이므로 불가능 출력
else:
    print("IMPOSSIBLE")