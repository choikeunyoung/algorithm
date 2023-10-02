N = int(input())

num_list = list(map(int,input().split()))
num_list.sort()
cnt = 0

for i in range(N-1):
    index = 1
    while i + index <= N-1:
        next = i + index
        left = 0
        right = N-1
        target = num_list[i] + num_list[next]
        while left <= right:
            mid = (left + right) // 2
            if num_list[mid] == target:
                if mid != i and mid != next:
                    cnt += 1
                break
            elif num_list[mid] < target:
                left = mid + 1
            elif num_list[mid] > target:
                right = mid - 1
        index += 1
print(cnt)