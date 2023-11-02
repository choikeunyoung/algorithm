N, k = map(int,input().split())
ans = 0
num = 1

while num <= N:
    ans += (N-num+1)
    num *= 10

if ans < k:
    print(-1)
else:
    