a, r, n = map(int,input().split())

cnt = 1

while True:
    a *= r
    cnt += 1
    if cnt == n:
        print(a)
        break