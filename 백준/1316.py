N = int(input())

cnt = 0
for _ in range(N):
    char = input()
    v_cnt = 0
    check_str = []
    for i in char:
        if i in check_str:
            if check_str[-1] == i:
                check_str.append(i)
            else:
                check_str.append("flag")
        else:
            check_str.append(i)
    if "flag" not in check_str:
        cnt += 1

print(cnt)