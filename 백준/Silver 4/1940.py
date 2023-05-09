N = int(input())
M = int(input())
check_list = list(map(int,input().split()))
cnt = 0
for i in range(len(check_list)):
    if check_list[i] != 0:
        for j in range(i,len(check_list)):
            check = check_list[i] + check_list[j]
            if check == M:
                cnt += 1
                check_list[i] = 0
                check_list[j] = 0
print(cnt,check_list)