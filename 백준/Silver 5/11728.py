A,N = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

C_list = A_list + B_list
C_list.sort()
print(*C_list)