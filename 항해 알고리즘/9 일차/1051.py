N, M = map(int,input().split())

matrix = [ list(map(int,input())) for _ in range(N)]

result = [1]

for i in range(N):
    for j in range(M):
        current = 1
        while i+current < N and j+current <M:
            if matrix[i][j] == matrix[i][j+current] and matrix[i][j] == matrix[i+current][j] and matrix[i][j] == matrix[i+current][j+current]:
                result.append(current+1)
            current += 1

answer = max(result)
print(answer**2)