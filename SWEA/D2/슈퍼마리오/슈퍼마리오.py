N = int(input())

num_list = [0] + list(map(int,input().split())) + ([-10002] * N)

current_index = 0
ans = 0

while current_index != N-1:
    if num_list[current_index+2] > num_list[current_index+7]:
        ans += num_list[current_index+2]
        current_index += 2
    elif num_list[current_index+2] < num_list[current_index+7]:
        ans += num_list[current_index+7]
        current_index += 7
print(ans)