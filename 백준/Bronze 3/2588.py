N = int(input())
M = str(input())

x = N*int(M[2])
y = N*int(M[1])
z = N*int(M[0])

print(x,y,z,(z*100+y*10+x), sep="\n")