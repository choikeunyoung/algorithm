N,K = map(int,input().split())

money = []
for _ in range(N):
    money.append(int(input()))
cnt = 0

while K>0:
    for i in range(len(money)-1,-1,-1):
        if K // money[i] > 0:
            cnt += (K // money[i])
            K %= money[i]
print(cnt)