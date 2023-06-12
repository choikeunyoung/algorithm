L,P = map(int,input().split())
num_list =list(map(int,input().split()))

check = L*P

for i in num_list:
    print(i-check,end=' ')