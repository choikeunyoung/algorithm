x,y = map(int,input().split())

x = bool(x)
y = bool(y)

print((x and (not y) or ((not x) and y)))