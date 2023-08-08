T = int(input())
cow = [list(map(int,input().split())) for _ in range(T)]

dict = {}
cnt_dict = {}
for i in cow:
    if i[0] in dict:
        if dict[i[0]] == i[1]:
            pass
        else:
            dict.update({i[0]:i[1]})
            cnt_dict[i[0]] += 1
    else:
        dict[i[0]] = i[1]
        cnt_dict[i[0]] = 0
sum = 0
for v in cnt_dict.values():
    sum += v
print(sum)