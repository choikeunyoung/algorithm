T = int(input())
for i in range(1,T+1):
    num_list = list(map(int,input().split()))
    total = 0
    for j in num_list:
        if j%2 == 1:
            total += j
    print(f"#{i}", total)