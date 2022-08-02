X,Y = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = set(A)
B = set(B)
print(len(A-B)+len(B-A))