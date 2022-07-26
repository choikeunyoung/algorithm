all_list=[]
for j in range(1,6):
    all_list.append(list(map(int,input().split())))
total = []
for i in all_list:
    total.append(sum(i))

print(total.index(max(total))+1,max(total))