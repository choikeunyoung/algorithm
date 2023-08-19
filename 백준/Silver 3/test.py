T = int(input())

for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    for i in range(N):
        visited = [ [False]*N for _ in range(N) ]
        stack = []
        
        for j in range(N):
