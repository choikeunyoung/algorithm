a,b,c = map(int,input().split())

if a == b == c:
    total = 10000 + (a*1000)
    print(total)
elif a == b:
    total = 1000 + (a)*100
    print(total)
elif a == c:
    total = 1000 + (a)*100
    print(total)
elif b == c:
    total = 1000 + (b)*100
    print(total)
else:
    total = max(a,b,c)*100
    print(total)

