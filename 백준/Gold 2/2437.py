N = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

min_weight = 0

for num in num_list:
    if min_weight +1 < num:
        break
    min_weight += num

print(min_weight + 1)