X = int(input())

cnt=0
for i in range(1,X+1):
    num_list=[]
    if i < 100:
        cnt+=1
    elif i <= 1000:
        num_list.append(i//100)
        i = i%100
        num_list.append(i//10)
        num_list.append(i%10)
        if num_list[1] - num_list[0] == num_list[2] - num_list[1]:
            cnt+=1
print(cnt)