N = int(input())
num_list = list(map(int,input().split()))
max_val = 0
total_num = 0
for i in num_list:
    if i > max_val:
        max_val = i

for i in range(len(num_list)):
    num_list[i] = num_list[i]/max_val*100
    total_num += num_list[i]

print(total_num/N)