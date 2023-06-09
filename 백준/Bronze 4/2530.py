hour_list = list(map(int, input().split()))
count = int(input())
sec = 0
min = 0


hour_list[2] = hour_list[2] + (count % 3600) % 60
if hour_list[2] >= 60:
    sec = hour_list[2] // 60
    hour_list[2] = hour_list[2] % 60

if sec != 0:
    hour_list[1] += sec

hour_list[1] = hour_list[1] + (count % 3600) // 60
if hour_list[1] >= 60:
    min = hour_list[1] // 60
    hour_list[1] = hour_list[1] % 60

if min != 0:
    hour_list[0] += min

hour_list[0] = hour_list[0] + count // 3600
if hour_list[0] >= 24:
    hour_list[0] = hour_list[0] % 24

print(*hour_list)
