import sys

input = sys.stdin.readline

N = int(input())

min_value = sys.maxsize
max_value = -sys.maxsize
total = 0
num_dict  = {}
check_list = []
num_list = []

for _ in range(N):
    num = int(input())
    if max_value < num:
        max_value = num
    if min_value > num:
        min_value = num
    
    total += num

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
    
    check_list.append(num)

check_list.sort()
max_count = max(num_dict.values())

for k,v in num_dict.items():
    if v == max_count and v != 1:
        num_list.append(k)
check_avg = total/N

if (check_avg//1)%2 ==0:
    check_avg = round(check_avg-1)+1
else:
    check_avg = round(check_avg)

if len(num_list) > 1:
    num_list.sort()
    print(check_avg)
    print(check_list[N//2])
    print(num_list[1])
    print(max_value-min_value)
else:
    print(check_avg)
    print(check_list[N//2])
    if len(num_list) == 0:
        if N != 1:
            print(check_list[1])
        else:
            print(check_list[-1])
    else:
        print(num_list[0])
    print(max_value-min_value)