N = int(input())
lope_list = []

for _ in range(N):
    lope_list.append(int(input()))

lope_list.sort(reverse=True)

check = 0
max_weight = 0

for i in range(N):
    if check == 0:
        min_num = lope_list[0]
        check += 1
        max_weight = min_num * 1
    else:
        if min_num > lope_list[i]:
            min_num = lope_list[i]
        if max_weight < min_num*(i+1):
            max_weight = min_num*(i+1)
print(max_weight)