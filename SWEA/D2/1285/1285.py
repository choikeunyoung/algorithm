T = int(input())
for i in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    total = 0
    cnt = 0
    for j in num_list:
        j = abs(0 - j)
        if total == 0:
            total = j
        else:
            if j < total:
                total = j
        
    for k in num_list:
        if abs(k) == total:
            cnt += 1
    print(f"#{i}", total, cnt)