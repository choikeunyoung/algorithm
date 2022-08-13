h,w = map(int,input().split())
matrix = [[0]*w for _ in range(h)]
n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    x -= 1
    y -= 1
    if d == 0:
        for k in range(l):
            matrix[x][y] = 1
            y+=1
    elif d == 1:
        for k in range(l):
            matrix[x][y] = 1
            x+=1

for j in matrix:
    for k in j:
        print(k,end=" ")
    print()