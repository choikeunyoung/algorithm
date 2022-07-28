N = int(input())
card_list=list(map(int,input().split()))
check_list ={}
M = int(input())
match_list=list(map(int,input().split()))

for k in check_list.keys():
    for l in card_list:
        if k == l:
            check_list[k] += 1
print(check_list)