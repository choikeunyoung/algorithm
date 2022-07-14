x,y = map(int,input().split())

x = bool(x)
y = bool(y)

print((x and y) or ((not x) and (not y)))