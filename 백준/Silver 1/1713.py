N = int(input())
M = int(input())
vote_list = list(map(str,input().split()))
old_list = []
num_list = [0]*101
picture = {}

for l in vote_list:
    if len(old_list) > N:
        cnt = 0
        min_cnt = num_list[old_list[0]]
        check = 0
        for i in range(1,len(old_list)):
            if num_list[old_list[i]] == min_cnt:
                cnt += 1
            elif num_list[old_list[i]] > min_cnt:
                min_cnt = num_list[old_list[i]]
                check = i
                cnt = 0
        print(cnt)
        if cnt >= 2:
            del_pop = old_list.pop(0)
            del picture[str(del_pop)]
            num_list[del_pop] = 0
        else:
            old_list.remove(check)
            del picture[str(check)]
            num_list[check] = 0
        if l in picture:
            num_list[int(l)] += 1
        else:
            picture[l] = 1
            num_list[int(l)] = 1
    else:
        if l in picture:
            num_list[int(l)] += 1
        else:
            picture[l] = 1
            old_list.append(int(l))
            num_list[int(l)] = 1
    print(old_list)
for k,y in enumerate(num_list):
    if y > 0:
        print(k)