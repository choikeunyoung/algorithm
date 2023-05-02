N,M = map(int,input().split())
# 방문 헀는지 체크하기 위한 리스트
visited = [[False] * M for _ in range(N)]

cnt = 0

dx = 1
dy = 1
# 타일의 종류
tile = [input() for _ in range(N)]
# 타일의 가로 세로만큼 반복문 진행
for i in range(N):
    for j in range(M):
        # stack 이라는 리스트 변수를 통해서 방문할 인덱스 체크
        stack = []
        # 만약 타일이 - 인경이와 ㅣ 인경우로 분리
        if tile[i][j] == "-":
            # 타일을 방문하지 않았을 경우만 조건실행
            if not visited[i][j]:
                # 방문했다는 표시를 남겨주고 cnt 라는 갯수변수를 1증가
                visited[i][j] = True
                cnt += 1
                # - 타일의 경우 우측으로 진행되기 때문에 우측으로 이동
                x = j + dx
                # 만약 M길이를 넘을 경우 stack 이라는 리스트에 추가하지않음
                if x < M:
                    stack.append(x)
                # stack이라는 리스트에 내용물이 있을경우 반복문 실행
                while stack:
                    # stack 에서 pop해온 값을 변수로 저장
                    next = stack.pop()
                    # 만약 다음 타일이 같은 - 인경우 방문했는지 체크한 후 다시 값을 1증가하고 M을 넘는지 확인
                    if tile[i][next] == "-":
                        if not visited[i][next]:
                            visited[i][next] = True
                            x = x + dx
                            if x < M:
                                stack.append(x)
        elif tile[i][j] == "|":
            if not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                y = i + dy
                if y < N:
                    stack.append(y)
                while stack:
                    next = stack.pop()
                    if tile[next][j] == "|":
                        if not visited[next][j]:
                            visited[next][j] = True
                            y = y + dy
                            if y < N:
                                stack.append(y)
print(cnt)