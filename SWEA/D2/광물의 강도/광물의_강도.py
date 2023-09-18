N, Q = map(int,input().split())

num_list = list(map(int,input().split()))
num_list.sort()
num_dict = {}

for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
