s=list(map(int,input().split()))
check_list = [1, 1, 2, 2, 2, 8]

for i in range(len(s)):
    if check_list[i] == s[i]:
        check_list[i] = 0
    else:
        check_list[i] = check_list[i] - s[i]
    print(check_list[i], end=" ")