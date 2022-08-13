x = int(input())

for i in range(1,x+1):
    cnt = 0
    for j in str(i):
        if '3' in j or '6' in j or '9' in j:
            cnt+=1
    if cnt > 0:
        print('X'*cnt, end=' ')
    else:
        print(i, end=' ')