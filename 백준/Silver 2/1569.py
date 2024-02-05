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
    # 최대 x, y / 최소 x, y 좌표 구하기
    y_total = max_y - min_y
    x_total = max_x - min_x
    #  x, y 좌표의 차이 값 구하기

# 정답 체크할 변수
flag = False

# y좌표 길이가 더 긴 경우
if y_total > x_total:
    # 두 좌표의 길이차 구해두기
    max_distance = y_total - x_total
    #  정사각형을 만드는 좌표 개수 체크
    cnt = 0
    for k in check_list:
        # y 좌표가 더 길기때문에 최대 x 좌표에서 길이 차만큼 더한 범위에 x값이 있고 y 좌표가 최대 or 최소 y인 경우 / 최대 최소 x 좌표값과 같고 최대 최소 y 좌표값 사이의 경우 cnt 값 증가
        if ((min_x <= k[0] <= max_x + max_distance) and ( min_y == k[1] or max_y == k[1])) or ((min_x == k[0] or max_x + max_distance == k[0]) and (min_y <= k[1] <= max_y)):
            cnt += 1
    # cnt 값이 N 과 같은 경우 정답을 출력할 변수 True
    if cnt == N:
        flag = True

    cnt = 0
    for k in check_list:
        # y 좌표가 더 길기때문에 최소 x 좌표에서 길이 차만큼 뺀 범위에 x값이 있고 y 좌표가 최대 or 최소 y인 경우 / 최대 최소 x 좌표값과 같고 최대 최소 y 좌표값 사이의 경우 cnt 값 증가
        if ((min_x - max_distance <= k[0] <= max_x) and (min_y == k[1] or max_y == k[1])) or ((min_x - max_distance == k[0] or max_x == k[0]) and (min_y <= k[1] <= max_y)):
            cnt += 1
    
    # cnt 값이 N 과 같은 경우 정답을 출력할 변수 True
    if cnt == N:
        flag = True
# x 좌표가 더 긴 경우
elif y_total < x_total:

    max_distance = x_total - y_total
    cnt = 0
    for k in check_list:
            # x 좌표가 더 길기때문에 최대 y 좌표에서 길이 차만큼 더한 범위에 y값이 있고 x 좌표가 최대 or 최소 x인 경우 / 최대 최소 y 좌표값과 같고 최대 최소 x 좌표값 사이의 경우 cnt 값 증가
        if (( min_x == k[0] or max_x == k[0] ) and (min_y <= k[1] <= max_y + max_distance)) or ((min_x <= k[0] <= max_x) and (min_y == k[1] or k[1] == max_y + max_distance)):
            cnt += 1

    if cnt == N:
        flag = True

    cnt = 0
    for k in check_list:
        # x 좌표가 더 길기때문에 최소 y 좌표에서 길이 차만큼 뺀 범위에 y값이 있고 x 좌표가 최대 or 최소 x인 경우 / 최대 최소 y 좌표값과 같고 최대 최소 x 좌표값 사이의 경우 cnt 값 증가
        if (( min_x == k[0] or max_x == k[0] ) and (min_y - max_distance <= k[1] <= max_y)) or ((min_x <= k[0] <= max_x ) and (min_y - max_distance == k[1] or max_y == k[1])):
            cnt += 1
    
    if cnt == N:
        flag = True

else:
    cnt = 0
    for k in check_list:
        # 길이가 같은 경우는 x 좌표 고정 y 범위 / y 좌표 고정 x 범위 만 확인해보면 된다.
        if (( min_x == k[0] or max_x == k[0]) and (min_y <= k[1] <= max_y)) or ((min_x <= k[0] <= max_x) and (min_y == k[1] or max_y == k[1])):
            cnt += 1
    if cnt == N:
        flag = True

if flag:
    print(max(y_total,x_total))
else:
    print(-1)