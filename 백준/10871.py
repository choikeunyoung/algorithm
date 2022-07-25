N,X = map(int,input().split())

# N_list=[]
# for i in range(0,N):
#     N_list.append(int(input()))

N_list = list(map(int,input().split()))

for k in N_list:
    if k < X:
        print(k, end=" ")