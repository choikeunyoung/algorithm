N = int(input())
num_list = list(map(int,input().split()))

num_list.sort()

left = 0
right = N - 1

target = 10**9
answer = []
if num_list[0] >= 0:
    answer = [num_list[0], num_list[1]]
elif num_list[-1] < 0:
    answer = [num_list[-2],num_list[-1]]
else:
    while left < right:
        value = num_list[left] + num_list[right]
        if abs(value) <= target:
            target = abs(value)
            answer = [num_list[left], num_list[right]]
        
        if value >= 0:
            right -= 1
        else:
            left += 1

print(*answer)