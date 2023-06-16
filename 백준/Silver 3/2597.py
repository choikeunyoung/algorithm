N = int(input())

left = 0
right = N
mid = (left+right)/2

red_point = sorted(list(map(int,input().split())))
blue_point = sorted(list(map(int,input().split())))
yellow_point = sorted(list(map(int,input().split())))


if red_point[0] != red_point[1]:
    check = (red_point[0]+red_point[1])/2
    if check > mid:
        if blue_point[0] >= check and blue_point[1] >= check:
            blue_point[0] = 0
            blue_point[1] = 0
        elif blue_point[0] <= check and blue_point[1] >= check:
            blue_point[1] = check-(blue_point[1]-check)
        if yellow_point[0] >= check and yellow_point[1] >= check:
            yellow_point[0] = 0
            yellow_point[1] = 0
        elif yellow_point[0] <= check and yellow_point[1] >= check:
            yellow_point[1] = check-(yellow_point[1]-check)
        right = check
    elif check <= mid:
        if blue_point[0] <= check and blue_point[1] <= check:
            blue_point[0] = 0
            blue_point[1] = 0
        elif blue_point[0] <= check and blue_point[1] >= check:
            blue_point[0] = check+(check-blue_point[0])
        if yellow_point[0] <= check and yellow_point[1] <= check:
            yellow_point[0] = 0
            yellow_point[1] = 0
        elif yellow_point[0] <= check and yellow_point[1] >= check:
            yellow_point[0] = check+(check-yellow_point[0])
        left = check

mid = (right+left)/2

if blue_point[0] != blue_point[1]:
    check = (blue_point[0]+blue_point[1])/2
    if check > mid:
        if yellow_point[0] >= check and yellow_point[1] >= check:
            yellow_point[0] = 0
            yellow_point[1] = 0
        elif yellow_point[0] <= check and yellow_point[1] >= check:
            yellow_point[1] = check-(yellow_point[1]-check)
        right = check
    elif check <= mid:
        if yellow_point[0] <= check and yellow_point[1] <= check:
            yellow_point[0] = 0
            yellow_point[1] = 0
        elif yellow_point[0] <= check and yellow_point[1] >= check:
            yellow_point[0] = check+(check-yellow_point[0])
        left = check

mid = (right+left)/2

if yellow_point[0] != yellow_point[1]:
    check = (yellow_point[0]+yellow_point[1])/2
    if check > mid:
        right = check
    elif check <= mid:
        left = check
answer = right-left
answer *= 10
if answer%2 == 0:
    answer /= 10
    print(f"{answer:.1f}")
else:
    answer -= 1
    answer /= 10
    print(f"{answer+0.1:.1f}")