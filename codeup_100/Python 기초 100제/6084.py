h,b,c,s = map(int,input().split())

total = round(h*b*c*s/8/1024/1024,1)
print(total, 'MB')