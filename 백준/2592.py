num_dict = {}
total_sum = 0
for _ in range(10):
    a = int(input())
    total_sum += a
    if a in num_dict:
        num_dict[a] += 1
    else:
        num_dict[a] = 1
avg_sum = total_sum//10
max_num = max(num_dict.values())
for k,v in num_dict.items():
    if v == max_num:
        print(avg_sum)
        print(k)
