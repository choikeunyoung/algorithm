matrix = [list(map(int,input().split())) for _ in range(9)]

sum_ = 0
index_ = [0, 0]
for i in range(9):
    for j in range(9):
        if matrix[i][j] > sum_:
            sum_ = matrix[i][j]
            index_[0] = i
            index_[1] = j
print(sum_)
print(index_[0]+1, index_[1]+1)