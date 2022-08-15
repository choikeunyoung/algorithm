from pprint import pprint
matrix = [list(map(int,input().split())) for _ in range(10)]
x = 1
y = 1
while True:
    matrix[x][y] = 9
    y += 1
    if matrix[x][y] == 1:
        y -= 1
        x += 1
        if matrix[x][y] == 1:
            x -= 1
            break
    if matrix[x][y] == 2:
        matrix[x][y] = 9
        break
for k in range(len(matrix)):
    for l in range(len(matrix)):
        print(matrix[k][l], end = ' ')
    print()