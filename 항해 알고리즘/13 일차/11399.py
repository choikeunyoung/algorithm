N = int(input())
total_min = 0
num_list = list(map(int,input().split()))
num_list.sort()
check = 0

for i in num_list:
    check += i
    total_min += check
print(total_min)