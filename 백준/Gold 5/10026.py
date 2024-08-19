def DFS(start, flag):
    # DFS 진행
    global count
    stack = [start]
    # 초기갑 선언
    visited[start[0]][start[1]] = True
    while stack:
        y,x = stack.pop()
        # 방향 배열 탐색
        for k in range(4):
            ny = y + direction[k][0]
            nx = x + direction[k][1]
            # 범위내 존재 시
            if 0 <= ny < N and 0 <= nx < N:
                # flag 변수를 통해 적녹색약 체크
                if flag == 0:
                    if not visited[ny][nx] and matrix[ny][nx] == matrix[y][x]:
                        stack.append((ny,nx))
                        visited[ny][nx] = True
                # 적록색약의 경우
                else:
                    # 방문하지 않았을때 R 값이 들어오면 matrix 값이 같거나 G 인 경우 스택 추가 후 방문 처리
                    if not visited[ny][nx]:
                        if matrix[y][x] == "R":
                            if matrix[ny][nx] == "G" or matrix[ny][nx] == matrix[y][x]:
                                stack.append((ny,nx))
                                visited[ny][nx] = True
                        # G가 들어온 경우 값이 같거나 R인 경우
                        elif matrix[y][x] == "G":
                            if matrix[ny][nx] == "R" or matrix[ny][nx] == matrix[y][x]:
                                stack.append((ny,nx))
                                visited[ny][nx] = True
                        # 외의 경우 스택에 그대로 추가
                        else:
                            if not visited[ny][nx] and matrix[ny][nx] == matrix[y][x]:
                                stack.append((ny,nx))
                                visited[ny][nx] = True
    count += 1

N = int(input())

direction = [(0,-1), (-1,0), (0,1), (1,0)]

matrix = [ list(map(str,input())) for _ in range(N) ]

count = 0

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS((i,j),0)
ans = count

count = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS((i,j),1)

print(ans, count)