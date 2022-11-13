N = int(input())

num_list = list(map(int,input().split()))

x = int(input())
cnt = 0
for i in num_list:
    if i == x:
        cnt += 1

print(cnt)