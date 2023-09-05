N, r, c = map(int,input().split())

matrix = [ [0] * 2**(N+1) for _ in range(2**(N+1))]

cnt = 0

direction = [(-1, -1), (-1, 0), (0, -1), (0, 0)]

def searching(pos, N):
    global cnt
    if N == 2:
        matrix[pos[0]][pos[1]] = cnt
        cnt += 1
        for dy, dx in direction:
            matrix[pos[0]+dx][pos[1]+dy] = cnt
            cnt += 1
    else:
        for i in range(4):
            

searching(([2**N],[2**N]),N)