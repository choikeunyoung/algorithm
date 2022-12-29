h,m = map(int,input().split())

if m-45 < 0:
    h -= 1
    if h < 0:
        print((24+h), (15+m))
    else:
        print(h, (15+m))
else:
    print(h, m-45)