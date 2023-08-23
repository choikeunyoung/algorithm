T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "o":
                