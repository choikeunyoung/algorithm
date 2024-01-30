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
    for k in check_list:
        if k[0]

else:
    for i in range(min_y, max_y+1 + (x_total - y_total)):
        square_point.add((min_x,i))
        square_point.add((max_x,i))


    for i in range(min_x+1, max_x):
        square_point.add((i,min_y))
        square_point.add((i,max_y + (x_total - y_total)))


if cnt == N:
    print(max(y_total,x_total))
else:
    print(-1)