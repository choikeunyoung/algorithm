N = int(input())

matrix = [list(map(str,input())) for _ in range(N)]
visited = [[False] * N for _ in range(N) ] 

dx = [-1,0,0,1]
dy = [0,-1,1,0]
total_length = []

for i in range(N):
    for j in range(N):
        stack = []
        if matrix[i][j] == "1":
            if not visited[i][j]:
                cnt = 1
                stack.append([i,j])
                while stack:
                    stack_list = stack.pop()
                    visited[stack_list[0]][stack_list[1]] = True
                    for i in range(4):
                        x = stack_list[1] + dx[i]
                        y = stack_list[0] + dy[i]
                        if (x >= 0 and x < N) and (y >= 0 and y < N):
                            if matrix[y][x] == "1":
                                if not visited[y][x] and [y,x] not in stack:
                                    stack.append([y,x])
                                    cnt += 1
                total_length.append(cnt)

print(len(total_length))
total_length.sort()

for i in total_length:
    print(i)