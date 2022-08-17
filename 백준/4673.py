list = [i for i in range(10001)]
new_list = []
for j in list:
    k = 0
    a = 0
    a = j
    sum_list = []
    while j:
        sum_list.append(j%10)
        j = j//10
    sum_list = sum(sum_list)
    k = a + sum_list
    if k in list:
        new_list.append(k)
new_list = set(new_list)
list = set(list)
a = sorted(list-new_list)
for l in a:
    print(l)