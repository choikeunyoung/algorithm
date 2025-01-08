N, M = map(int,input().split())

matrix = [[0]*(M+1)]

for _ in range(N):
    matrix.append([0] + list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,M+1):
        matrix[i][j] = matrix[i][j] + max(matrix[i-1][j],matrix[i][j-1])
        
print(matrix[i][j])