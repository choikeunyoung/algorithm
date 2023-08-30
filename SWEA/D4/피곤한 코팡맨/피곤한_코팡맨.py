def BFS(pos):
    


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