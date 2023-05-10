N = int(input())
M = int(input())
check_list = list(map(int,input().split()))
check_list.sort()

i = 0
j = N-1
cnt = 0
while i < j:
    if check_list[i] + check_list[j] < M:
        i += 1
    elif check_list[i] + check_list[j] == M:
        cnt += 1
        i += 1
        j -= 1
    else:
        j -= 1
print(cnt)