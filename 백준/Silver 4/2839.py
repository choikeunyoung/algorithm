N = int(input())
cnt = 0

if N%5 == 0:
    print(N//5)
elif N < 5:
    if N == 3:
        print(N//3)
    else:
        print(-1)
else:
    check = N // 5
    remain = N % 5
    while True:
        if remain % 3 == 0:
            print(check + remain//3)
            break
        else:
            remain += 5
            check -= 1
            if remain > N:
                print(-1)
                break