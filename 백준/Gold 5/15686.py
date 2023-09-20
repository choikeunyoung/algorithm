def check_value(first_list, second_list):
    ans = 0
    for i in first_list:
        for j in second_list:
            visited[j[0]][j[1]] = min(visited[j[0]][j[1]],abs(i[0]-j[0])+abs(i[1]-j[1]))
one_pos = []
two_pos = []

N, M = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [10**6] * N for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            one_pos.append((i,j))
        elif matrix[i][j] == 2:
            two_pos.append((i,j))

min_value = 10**6
check = []

for i in two_pos:
    total = 0
    for j in one_pos:
        total += (abs(i[0]-j[0])+abs(i[1]-j[1]))
    check.append(total)
    
if len(check) == M:
    check_value(two_pos,one_pos)
else:
    ans = []
    while M > 0:
        min_check = min(check)
        for i in range(len(check)):
            if check[i] == min_check:
                check.pop(i)
                ans.append(two_pos[i])
                break
        M -= 1    
    print(ans, two_pos, check)
    check_value(ans,one_pos)
answer = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] != 10**6:
            answer += visited[i][j]
print(answer)