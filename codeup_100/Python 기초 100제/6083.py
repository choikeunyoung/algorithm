r,g,b = map(int,input().split())
cnt = 0
for i in range(r):
    for k in range(g):
        for l in range(b):
            print(i, k, l)
            cnt+=1
print(cnt)