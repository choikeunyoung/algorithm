N,M = map(int,input().split())
current_x = 0
current_y = M
n_check = 0
m_check = 0

matrix = [[0] * N for _ in range(M)]

while N == 0 and M == 0:
    if n_check == 0 and m_check == 0:
        for i in range(N):
            matrix[current_x][current_y] = 1
            current_y += 1