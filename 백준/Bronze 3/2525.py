h,m = map(int,input().split())
time = int(input())

while time > 0:
    if time >= 60:
        h += 1
        if h >= 24:
            h = 0
    else:
        if m+time >= 60:
            h += 1
            m = (m+time)-60
            if h>=24:
                h = 0
        else:
            m += time
    time -= 60
print(h, m)