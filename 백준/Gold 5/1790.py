N, k = map(int,input().split())
ans = 0
num = 1

while num <= N:
    ans += (N-num+1)
    num *= 10
print(ans)
if N >= 10:
    num //= 10
    check = ans - (N-(num+1))
    k -= (num+1)
    num_length = len(str(num))
    answer = k%num_length
    print(k, check)
    if k > check:
        print(-1)
    else:
        if answer == 0:
            num += (k//num_length)
        else:
            num += (k//num_length) + 1
        num = str(num)
        print(num[answer])
else:
    if N < k:
        print(-1)
    else:
        print(N)