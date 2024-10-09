N, r, c = map(int, input().split())

matrix = [0]* (2 ** N + 1)

cnt = 0

def searching(pos, N):
    global cnt
    if N == 1:
        matrix[pos[0]][pos[1]] = cnt
        cnt += 1
    else:
        half = 2**(N-1)
        if pos[0] < half and pos[1] < half:
            searching((pos[0],pos[1]),N-1)
        elif pos[0] < half and pos[1] >= half:
            searching((pos[0],pos[1]+1),N-1)
        elif pos[0] >= half and pos[1] < half:
            
        elif pos[0] >= half and pos[1] >= half:
        



searching(([2**N, 2**N]), N)
print(matrix)