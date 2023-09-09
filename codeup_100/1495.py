N, M, K = map(int,input().split())
matrix = [ [0]*M for _ in range(N) ]

total_sum = [ [0] * M for _ in range(N) ]

for tc in range(K):
    x1, y1, x2, y2, u = map(int,input().split())
    matrix[x1][y1] = matrix[x1][y1]+u
    if x2+1 < N and y2 + 1< M:
        matrix[x2+1][y2+1] = matrix[x2+1][y2+1]+u
        matrix[x1][y2+1] = matrix[x1][y2+1]-u
        matrix[x2+1][y1] = matrix[x2+1][y1]-u

garo_total = 0
for i in range(N):
    for j in range(M):
        garo_total += matrix[i][j]
        total_sum[i][j] = garo_total

sero_total = 0
for j in range(M):
    for i in range(N):
        sero_total += total_sum[i][j]
        total_sum[i][j] = sero_total

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()

print()

for i in total_sum:
    for j in i:
        print(j, end=" ")
    print()