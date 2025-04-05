N, M = map(int,input().split())
num_list = list(map(int,input().split()))

max_value = max(num_list)

left = 0
right = max(num_list)
answer = right
cnt = 0
while left <= right:
    middle = (left+right) // 2

    low_value = num_list[0]
    high_value = num_list[0]
    check = 1

    for num in num_list:
        if high_value < num:
            high_value = num
        
        if low_value > num:
            low_value = num
        
        if high_value - low_value > middle:
            check += 1
            low_value = num
            high_value = num
    
    if M >= check:
        right = middle - 1
        answer = min(answer,middle)
    else:
        left = middle + 1

print(answer)