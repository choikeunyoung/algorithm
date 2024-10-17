from itertools import combinations
# DFS 로직
def DFS(start):
    stack = [start]
    global max_value
    global check_cnt
    while stack:
        next = stack.pop()
        for k in range(4):
            ny = next[0] + direction[k][0]
            nx = next[1] + direction[k][1]
            if 0 <= ny < N and 0 <= nx < M:
                if virus[ny][nx] == 0:
                    virus[ny][nx] = 3
                    check_cnt -= 1
                    stack.append((ny,nx))



N, M = map(int,input().split())

zero_cnt = 0
check_cnt = 0
max_value = 0
direction = [(0,-1),(-1,0),(0,1),(1,0)]
matrix = []
# 들어온 인풋값을 저장 한 후 0의 총 개수 체크
for _ in range(N):
    check_list = list(map(int,input().split()))
    matrix.append(check_list)
    zero_cnt += check_list.count(0)
# 0의 위치, 바이러스의 위치 체크 변수
zero_pos = []
two_pos = []
# 0의 위치와 바이러스 위치를 저장
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zero_pos.append((i,j))
        elif matrix[i][j] == 2:
            two_pos.append((i,j))
# 0의 위치중 3개를 고를 수 있는 모든 경우를 조합
combination_list = list(combinations(zero_pos[:],3))
# 조합 리스트 순회
for comb in combination_list:
    # check 변수를 통해 0의 개수 저장
    check_cnt = zero_cnt
    # virus 라는 리스트를 새로 생성
    virus = []
    # virus 리스트에 바이러스 위치 저장
    for _ in range(N):
        virus.append(matrix[_][:])
    # 0의 위치들 중 3개 조합한 리스트 순회
    for com in comb:
        # 바이러스 리스트 좌표에 1 대입 후 0의 개수 -1 총 3개 빼줌
        virus[com[0]][com[1]] = 1
        check_cnt -= 1
    # 바이러스 위치 순회
    for pos in two_pos:
        DFS(pos)
    # 최종 0의 개수 최대 값 비교
    if check_cnt > max_value:
        max_value = check_cnt

print(max_value)