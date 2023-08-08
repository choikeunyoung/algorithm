T = int(input())

for __ in range(T):
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for k in range(n-1):
        for i in range(m):
            for j in range(n-1):
                if matrix[j][i] == 1:
                    if matrix[j+1][i] == 1:
                        pass
                    else:
                        matrix[j+1][i] = 1
                        matrix[j][i] = 0
                        cnt+=1

    print(cnt)