N,M = map(int,input().split())
no_hear = {}
no_see = {}
no_see_hear = []
cnt = 0
for i in range(N):
    hear = input()
    if hear not in no_hear:
        no_hear[hear] = 0
for j in range(N+1,N+M):
    see = input()
    if see not in no_see:
        no_see[see] = 0
for k in no_hear.keys():
    if k in no_see:
        no_see_hear.append(k)
        cnt += 1
print(cnt)
for x in sorted(no_see_hear):
    print(x)