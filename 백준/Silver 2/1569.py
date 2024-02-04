import sys

input = sys.stdin.readline

N = int(input())

square_point = set()

min_x = sys.maxsize
max_x = -sys.maxsize
min_y = sys.maxsize
max_y = -sys.maxsize

check_list = []

for _ in range(N):
    point = tuple(map(int,input().split()))
    check_list.append(point)
    min_x = min(min_x, point[0])
    min_y = min(min_y, point[1])
    max_x = max(max_x, point[0])
    max_y = max(max_y, point[1])

    y_total = max_y - min_y
    x_total = max_x - min_x

cnt = 0

if y_total > x_total:
    max_distance = y_total - x_total
    for k in check_list:
        if (min_x <= k[0] <= max_x + max_distance and ( min_y == k[1] or max_y == k[1] + max_distance)) or (min_x - max_distance <= k[0] < min_x and  (min_y == k[1] or max_y == k[1] + max_distance)):
            cnt += 1

elif y_total < x_total:
    max_distance = x_total - y_total
    for k in check_list:
        if (( min_x == k[0] or max_x == k[0] ) and min_y <= k[1] <= max_y + (x_total - y_total)) or (( min_x == k[0] or max_x == k[0] ) and min_y - (x_total - y_total) <= k[1] < min_y ):
            cnt += 1

else:
    for k in check_list:
        if (( min_x == k[0] or max_x == k[0]) and (min_y <= k[1] <= max_y)) or ((min_x <= k[0] <= max_x) or (min_y == k[1] or max_y == k[1])):
            cnt += 1
            print(k)


if cnt == N:
    print(max(y_total,x_total))
else:
    print(-1)