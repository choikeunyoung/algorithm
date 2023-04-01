N,P,limit = map(int,input().split())

num_list = list(map(int,input().split()))

num_list.sort(reverse=True)

rank_list = []

for i in num_list:
    if len(rank_list) == limit:
