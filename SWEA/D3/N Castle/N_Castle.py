def castle(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for i in range(N):
        if matrix[i] == 1:
            continue
        matrix[i] = 1
        castle(row+1)
        matrix[i] = 0

N = int(input())

matrix = [0]*N
cnt = 0

castle(0)
print(cnt)