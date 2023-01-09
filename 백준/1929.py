N,M = map(int,input().split())

num_list = [True] * 1000000
pri_list = []

for j in range(2,round(len(num_list)**0.5)):
    if num_list[j] == True:
        for k in range(2*j, len(num_list), j):
            num_list[k] = False

flag = 0

for l in range(2,len(num_list)):
    if num_list[l] == True:
        if N <= l and l <= M:
            print(l)