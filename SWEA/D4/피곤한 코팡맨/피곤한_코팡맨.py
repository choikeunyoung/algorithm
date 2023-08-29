N = int(input())
matrix = [ list(map(str,input())) for _ in range(N) ]
matrix_index = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [False]*N for _ in range(N) ]

dx = [-1, 0, 1, -1, 1, -1, 0 ,1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
k_cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == "K":
            k_cnt += 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == "P":
            min_value = matrix_index[i][j]
            max_value = matrix_index[i][j]
            visited[i][j] = True
            ans_list = []
            cnt = 0
            queue = [(i,j)]
            while queue:
                check = queue.pop(0)
                visited[check[0]][check[1]] = True
                for k in range(8):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if ( 0 <= nx < N ) and ( 0 <= ny < N ):
                        
                if cnt == k_cnt:
                    break
print(max_value-min_value)