n, m = map(int,input().split())
num_list = list(map(int,input().split()))
num_length = len(num_list)
cnt = 0

low = 0
total = num_list[low]
high = low+1

while True:
    total += num_list[high]
    if total > m:
        low += 1
        high = low + 1
        total = num_list[low]
        if total == m:
            cnt += 1
            low += 1
            high = low + 1
            total = num_list[low]
    elif total < m:
        high += 1
    elif total == m:
        cnt += 1
        low += 1
        high = low + 1
        total = num_list[low]
        if total == m:
            cnt += 1
            low += 1
            high = low + 1
            total = num_list[low]
        
    if high >= n:
        break
print(cnt)