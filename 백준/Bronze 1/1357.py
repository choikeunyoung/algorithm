def Rev(x):
    x = str(x)
    x = x[::-1]
    for i in x:
        if x == '0':
            x.replace('0',"")
    return int(x)

X,Y = map(int,input().split())
print(Rev(Rev(X)+Rev(Y)))

