N, start, end = map(int,input().split())

matrix = [ [0] * (N+1) for _ in range(N+1) ]
visited = [False]*(N+1)

for _ in range(N-1):
    A,B,C = map(int,input().split())
    matrix[A][B] = C
    matrix[B][A] = C
