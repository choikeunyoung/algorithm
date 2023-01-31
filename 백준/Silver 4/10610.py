N = input()
num_list = []

total = 0
ans = ""
if int(N) < 30:
    print(-1)
else:
    for i in N:
        total += int(i)
        num_list.append(i)
    num_list.sort(reverse=True)
    if num_list[-1] != "0":
        print(-1)
    else:
        if total % 3 != 0:
            print(-1)
        else:
            for k in num_list:
                ans += k
            print(ans)