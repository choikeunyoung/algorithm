def pel(num, check):
    if check > 10000000:
        check = 10000000
    prime = [True]*(check+1)
    pel = [True]*(check+1)
    for i in range(2,check+1):
        if str(i) == str(i)[::-1]:
            pel[i] = False
        if prime[i]:
            for k in range(2*i, check+1,i):
                prime[k] = False
    
    return [ l for l in range(num, check+1) if prime[l] and not pel[l]]
            
n,m = map(int,input().split())

pel_list = pel(n,m)

for i in pel_list:
    print(i)
print(-1)