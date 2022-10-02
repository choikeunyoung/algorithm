N = int(input())
matrix_1 = [list(map(str, input())) for _ in range(N)]
matrix_2 = [list(map(str, input())) for __ in range(N)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

check_matrix = [[0] * N for _ in range(N)]
check = 0
for i in range(N):
    for j in range(N):
        if matrix_1[i][j] == "." and matrix_2[i][j] == "x":
            for k in range(len(dx)):
                x = i + dx[k]
                y = j + dy[k]
                if (x >= 0 and y >= 0) and (x <= N - 1 and y <= N - 1):
                    if matrix_1[x][y] == "*":
                        check_matrix[i][j] += 1
        elif matrix_1[i][j] == "." and matrix_2[i][j] == ".":
            check_matrix[i][j] = "."
        elif matrix_1[i][j] == "*" and matrix_2[i][j] == ".":
            check_matrix[i][j] = "."
        elif matrix_1[i][j] == "*" and matrix_2[i][j] == "x":
            check_matrix[i][j] = "*"
            check = 1
print(check_matrix)
if check != 1:
    for i in check_matrix:
        for j in i:
            print(j, end="")
        print()
else:
    for i in range(len(check_matrix)):
        for j in range(len(check_matrix)):
            if check_matrix[i][j] == "." and matrix_1[i][j] == "*":
                print("*", end="")
            elif check_matrix[i][j] == "." and matrix_1[i][j] != "*":
                print(".", end="")
            else:
                print(check_matrix[i][j], end="")
        print()
