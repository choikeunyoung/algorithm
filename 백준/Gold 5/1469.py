N = int(input())
num_list = list(map(int,input().split()))

num_list.sort()

num_dict = {}

for i in num_list:
    num_dict[i] = 2
