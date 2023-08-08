N = int(input())
milks = list(map(int,input().split()))
milk_list = []
cnt = 0
for i in milks:
    if len(milk_list) == 3:
        milk_list.clear()
    if len(milk_list) == 0 and i == 0:
        milk_list.append(i)
        cnt += 1
    elif len(milk_list) == 1 and i == 1:
        milk_list.append(i)
        cnt += 1
    elif len(milk_list) == 2 and i == 2:
        milk_list.append(i)
        cnt += 1
print(cnt)