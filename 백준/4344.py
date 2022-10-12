C = int(input())

for i in range(1,C+1):
    info_list = list(map(int,input().split()))
    cnt = 0
    total = 0
    for i in info_list[1:]:
        total += i
    total_avg = total/info_list[0]

    for i in info_list[1:]:
        if i > total_avg:
            cnt += 1
    ans = round(cnt/info_list[0] * 100,3)
    print(f"{ans:.3f}%")