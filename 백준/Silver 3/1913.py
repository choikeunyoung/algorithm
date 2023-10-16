N = int(input())
search = int(input())

start = N*N
direction = [1, 1, -1, -1]
matrix = [ [0] * N for _ in range(N)]
pos = [0,0]
index = 0
while start != 0:
    matrix[pos[0]][pos[1]] = start
    if index % 2 == 0:
        if 0 <= pos[0] < N-1:
            pos[0] += direction[index]
        else:
            index = (index+1)%4
    else:
        if 0 <= pos[1] < N-1:
            pos[1] += direction[index]
        else:
            index = (index+1)%4
    start -= 1
    print(matrix)