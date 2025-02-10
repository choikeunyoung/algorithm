N = int(input())

if N == 0:
    print(0)
else:
    start = 1
    cnt = 1

    while start < N:
        start *= 2
        cnt+=1
    print(cnt)