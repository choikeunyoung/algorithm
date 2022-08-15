n = int(input())

matrix = [[0] * 19 for _ in range(19)]

for i in range(n):
    x,y = map(int,input().split())
    matrix[x-1][y-1] = 1

for j in range(len(matrix)):
    for k in range(len(matrix)):
        print(matrix[j][k], end = ' ')
    print()