x = int(input())
y = len(str(x))
z = []
s = 0
while x!=0:
    z.append(x%10)
    x=x//10

for i in z:
    print(i,end="")