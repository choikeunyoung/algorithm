N = int(input())
num_list = set([])
for i in range(N):
    A,B = map(int,input().split())
    for j in range(A,10+A):
        for k in range(B,10+B):
            num_list.add((j,k))

print(len(num_list))