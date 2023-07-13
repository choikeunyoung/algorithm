import sys

N = int(input())

min_value = sys.maxsize
min_index = 0

num_list = list(map(int,input().split()))
num_list.sort()

max_value = sys.maxsize
max_index = max(num_list)

check_list= []

left = 0
right = N

while left <= right:
    check = 0
    middle = (left+right)//2
    for i in num_list:
        check += abs(i-num_list[middle])
    
    if check <= max_value:
        max_value = check
        max_index = min(max_index,num_list[middle])
        right = middle-1
    else:
        left = middle+1
print(max_index)