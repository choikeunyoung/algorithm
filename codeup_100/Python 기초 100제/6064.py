a, b, c = map(int,input().split())

if a > b and b > c:
    print(c)
elif a > b and b < c:
    print(b)
elif b > a and a < c:
    print(a)
elif b > a and a > c:
    print(c)
elif c > a and a > b:
    print(b)
elif c > a and a < b:
    print(a)
else:
    print(a)