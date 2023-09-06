N, r, c = map(int, input().split())

matrix = [0]* (2 ** N + 1)

cnt = 0

direction = [(-1, -1), (-1, 0), (0, -1), (0, 0)]


def searching(pos, N):
    global cnt
    if N == 1:
        for dy, dx in direction:
            matrix[pos[0] + dy][pos[1] + dx] = cnt
            cnt += 1
    else:
        searching([pos[0]//2, pos[1]//2],N-1)
        searching([pos[0]//2, pos[1]],N-1)
        searching([pos[0], pos[1]//2],N-1)
        searching([pos[0], pos[1]],N-1)

searching(([2**N, 2**N]), N)
print(matrix)