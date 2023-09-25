from collections import deque
# 방향 배열
direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def BFS(start):
    global max_value
    # 덱생성
    q = deque([start])
    while q:
        check = q.popleft()
        # 방향배열 순회
        for k in range(8):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            # 범위내 존재할 경우
            if ( 0 <= ny < N ) and ( 0 <= nx < M ):
                # matrix 값이 0인 경우
                if matrix[ny][nx] == 0:
                    # 이전값 +1 로 구현
                    matrix[ny][nx] = matrix[check[0]][check[1]] + 1
                    # q에 값 추가
                    q.append((ny,nx))
                # matrix 값이 아닌 경우
                else:
                    # matrix에 저장된 값이랑 이전값 +1 한 값을 비교하여 작은 경우
                    if matrix[ny][nx] > matrix[check[0]][check[1]] + 1:
                        # q에 추가 및 값 갱신
                        q.append((ny,nx))
                        matrix[ny][nx] = matrix[check[0]][check[1]] + 1

N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
one_pos = []
# 1인 지점 찾는 반복문
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            one_pos.append((i,j))
# 최고 값 갱신 변수
max_value = 0
# one_pos 에서 1인 지점 값 뽑아내며 반복
for l in one_pos:
    BFS(l)
# matrix[i][j] 값이 max_value 보다 크면 값 갱신
for i in range(N):
    for j in range(M):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

print(max_value-1)