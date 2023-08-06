T = int(input())

dx = [-1, 1, -1, 1]
dy = [-1, -1, 1, 1]

for i in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    print(visted)
    answer = 0
    for i in range(N):
        num_list = []
        stack = []
        for j in range(N):
            visted = [[False] * N for _ in range(N)]
            num_list.append(matrix[i][j])
            visted[i][j] = True
            for k in range(4):
                x = j + dx[k]
                y = i + dy[k]
                if (0 <= x < N) and (0 <= y < N):
                    stack.append([y, x])
                    while stack:
                        next = stack.pop()
                        visted[next[0]][next[1]] = True
                        if matrix[next[0]][next[1]] not in num_list:
                            num_list.append(matrix[next[0]][next[1]])
                            