N = int(input())
check_list = []
for _ in range(N):
    check_list.append(list(map(str,input())))
for i in range(len(check_list[0])):
    check_str = ""
    cnt = 0
    for j in range(len(check_list)):
        if check_str == "":
            check_str = check_list[j][i]
        else:
            if check_str == check_list[j][i]:
                cnt += 1
    if cnt == N-1:
        print(check_list[j][i], end="")
    else:
        print("?", end="")