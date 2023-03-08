N,M = map(int,input().split())

num_list = []

for i in range(1,N+1):
    num_list.append(i)

for _ in range(M):
    temp1, temp2 = map(int,input().split())
    temp = num_list[temp1-1]
    num_list[temp1-1] = num_list[temp2-1]
    num_list[temp2-1] = temp

print(*num_list)