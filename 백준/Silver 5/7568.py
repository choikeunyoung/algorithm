N = int(input())
all_list=[]
cnt_list=[]
for i in range(1,N+1):
    all_list.append(list(map(int,input().split())))
    cnt_list.append(0)

for i in range(0,len(all_list)):
    for j in range(0,len(all_list)):
        if all_list[i][0] > all_list[j][0] and all_list[i][1] > all_list[j][1]:
            cnt_list[j] += 1

for k in cnt_list:
    print(k+1,end=' ')
