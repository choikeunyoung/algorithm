N,M = map(int,input().split())
no_hear = []
no_see = []
no_hear_see = []
cnt = 0

for i in range(N):
    no_hear.append(input())
for j in range(N,N+M):
    no_see.append(input())
for k in no_hear:
    if k in no_see:
        no_hear_see.append(k)
        cnt += 1
print(cnt)
no_hear_see.sort()
for p in no_hear_see:
    print(p)