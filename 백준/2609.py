a, b = map(int,input().split())

if a > b:
    if a % b == 0:
        print(b)
        print(a)
    else:
        for i in range(1,b):
            if b % i == 0 and a % i == 0:
                c = i
        print(c)
        print(a*b//c)
else:
    if b % a == 0:
        print(a)
        print(b)
    else:
        for i in range(1,a):
            if b % i == 0 and a % i == 0:
                c = i
        print(c)
        print(a*b//c)