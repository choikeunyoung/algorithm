N = int(input())
num_list = list(map(int, input().split()))
cnt = 0
for i in num_list:
    if i % 10 == N:
        cnt += 1
print(cnt)
