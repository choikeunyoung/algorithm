N = int(input())

have_dict = {}

for i in range(N):
    have_dict[int(input())] = 0

M  = int(input())

check_list = list(map(int,input().split()))

for i in range(len(check_list)):
    for j in range(len(have_list)):
        if check_list[i] == have_list[j]:
            print("1",end=" ")
            break
    else:
        print("0",end=" ")