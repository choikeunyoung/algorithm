N = int(input())
max_value = []
for _ in range(N):
    num_list = list(map(int, input().split()))
    max_num = 0
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                check = num_list[i] + num_list[j] + num_list[k]
                if check % 10 >= max_num:
                    max_num = check % 10
                    check_list = [max_num, check]
    max_value.append(check_list)
max_check = max(max_value)[0]
pos = 0
value_check = 0

for j, e in enumerate(max_value):
    if e[0] == max_check:
        if e[1] > value_check:
            pos = j

print(pos + 1)
