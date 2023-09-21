from itertools import combinations


# 들어온 리스트들을 바탕으로 visited 값 갱신해주는 함수
def check_value(first_list, second_list):
    for i in first_list:
        for j in second_list:
            visited[j[0]][j[1]] = min(
                visited[j[0]][j[1]], abs(i[0] - j[0]) + abs(i[1] - j[1])
            )


# 1의 위치, 2의 위치 저장할 리스트
one_pos = []
two_pos = []

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 행렬 순회하며 1의 좌표와 2의 좌표를 저장
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            one_pos.append((i, j))
        elif matrix[i][j] == 2:
            two_pos.append((i, j))
# 2의 위치 리스트로 M만큼 조합 생성
two_pos = list(combinations(two_pos, M))
# 최소값 저장 할 변수
ans = 10**6
# 2가 저장된 조합 리스트를 순회하며
for i in two_pos:
    # 거리가 어느정도 되는지 체크할 vistied
    visited = [[10**6] * N for _ in range(N)]
    # 함수에 i 조합과 1의 좌표를 넣어 visited 계산
    check_value(i, one_pos)
    # 임시 변수 생성
    answer = 0
    for i in range(N):
        for j in range(N):
            # 거리값들을 임시변수에 더해줌
            if visited[i][j] != 10**6:
                answer += visited[i][j]
    # 게산이 끝난 임시변수가 최소값보다 작은 경우 값 갱신
    if answer < ans:
        ans = answer

print(ans)
