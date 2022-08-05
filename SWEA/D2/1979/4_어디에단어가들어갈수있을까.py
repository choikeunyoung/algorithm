import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(sys.stdin.readline())

for i in range(1,T+1):
    n,k = list(map(int,sys.stdin.readline().split()))
    matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    vertical = [[] for __ in range(n)]
    horizon = [[] for __0 in range(n)]
    for x in range(0,len(matrix)):
        cnt = 0
        for y in range(0,len(matrix)):
            if matrix[x][y] == 1:
                cnt+=1
                if y == len(matrix)-1:
                    horizon[x].append(cnt)
            elif matrix[x][y] == 0:
                if cnt > 0:
                    horizon[x].append(cnt)
                cnt = 0
    
    for a in range(0, len(matrix)):
        cnt = 0
        for b in range(0,len(matrix)):
            if matrix[b][a] == 1:
                cnt+=1
                if b == len(matrix)-1:
                    vertical[a].append(cnt)
            elif matrix[b][a] == 0:
                if cnt > 0:
                    vertical[a].append(cnt)
                cnt = 0
        
    total_cnt = 0
    for l in horizon:
        total_cnt += l.count(k)
    for p in vertical:
        total_cnt += p.count(k)
    print(f"#{i}", total_cnt)