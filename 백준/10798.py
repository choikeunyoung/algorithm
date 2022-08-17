matrix = [list(map(str,input())) for _ in range(5)]
new_matrix = str()
max_len = []

for i in matrix:
    max_len.append(len(i))

len_matrix = max(max_len)

for j in range(len_matrix):
    for i in range(len(matrix)):
        try:
            new_matrix += matrix[i][j]
        except IndexError:
            continue
print(new_matrix)