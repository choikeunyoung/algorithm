from pprint import pprint
matrix = [list(map(int,input().split())) for _ in range(19)]

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    for j in range(19):
        if matrix[j][y-1] == 0:
            matrix[j][y-1] = 1
        else:
            matrix[j][y-1] = 0
        if matrix[x-1][j] == 1:
            matrix[x-1][j] = 0
        else:
            matrix[x-1][j] = 1
for k in range(len(matrix)):
    for p in range(len(matrix)):
        print(matrix[k][p], end=' ')
    print()