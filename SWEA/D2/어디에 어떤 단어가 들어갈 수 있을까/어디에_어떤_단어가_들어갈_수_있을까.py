T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        if cnt == K:
            answer += 1
    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        if cnt == K:
                    answer += 1

    print(f"#{tc} {answer}")