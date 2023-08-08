N = int(input())

num_list = list(map(int,input().split()))
cnt = 0
for i in num_list:
    if i <= 1:
        continue
    else:
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            cnt += 1
print(cnt)