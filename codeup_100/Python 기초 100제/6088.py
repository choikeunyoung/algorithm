a, d, n = map(int,input().split())

cnt = 1

while True:
    a += d
    cnt += 1
    if cnt == n:
        print(a)
        break