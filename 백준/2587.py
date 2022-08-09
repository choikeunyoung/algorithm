sum_list=[]
for i in range(5):
    sum_list.append(int(input()))
sum_list.sort()
total = sum(sum_list)
print(round(total/len(sum_list)))
print(sum_list[2])
