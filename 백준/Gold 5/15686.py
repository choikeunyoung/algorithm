from itertools import combinations

def check_value(first_list, second_list):
    for i in first_list:
        for j in second_list:
            visited[j[0]][j[1]] = min(visited[j[0]][j[1]], abs(i[0] - j[0]) + abs(i[1] - j[1]))

one_pos = []
two_pos = []

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            one_pos.append((i, j))
        elif matrix[i][j] == 2:
            two_pos.append((i, j))

min_value = 10**6
two_pos = list(combinations(two_pos,M))
ans = 10**6
for i in two_pos:
    visited = [[10**6] * N for _ in range(N)]
    check_value(i, one_pos)
    answer = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 10**6:
                answer += visited[i][j]
    if answer < ans:
        ans = answer

print(ans)
