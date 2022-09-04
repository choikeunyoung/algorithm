n=int(input())
h=[]
l=[]

a=list(map(int,input().split()))
for i in range(n-1):
    if a[i]<a[i+1]:
        l.append(a[i])
    else:
        l.append(a[i])
        h[j]=max(l)-min(l)
        l.clear()

print(max(h))