T = int(input())
b = T
cnt = 0
while True:
    if b < 10:
        x = b+0
    else:
        x = b//10 + b%10
    div_ = b%10
    x = x%10
    b = div_*10+x
    cnt+=1
    if b == T:
        print(cnt)
        break