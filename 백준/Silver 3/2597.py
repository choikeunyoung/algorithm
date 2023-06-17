N = int(input())

left = 0
right = N
# 점을 순서별로 리스트로 오름차순 정렬하여 받음
red_point = sorted(list(map(int,input().split())))
blue_point = sorted(list(map(int,input().split())))
yellow_point = sorted(list(map(int,input().split())))
# 접히는 길이를 담을 변수
fold_length = 0

# 두 점의 위치가 다를 경우
if red_point[0] != red_point[1]:
    # 두 점의 접히는 점을 mid 변수로 받아옴
    mid = (red_point[0]+red_point[1])/2
    # 접히는 길이는 두 점의 중앙값 - left 값
    fold_length = mid - left
    # 만약 파란점, 노란점 각각 위치가 접히는 mid 값보다 작은 경우
    # 왼쪽을 기준으로 접기때문에 mid 라는 변수에 각각의 점들간의 거리를 계산 후 더한 값을 각각 점에 대입
    if blue_point[0] < mid:
        blue_point[0] = mid + (mid-blue_point[0])
    if blue_point[1] < mid:
        blue_point[1] = mid + (mid-blue_point[1])
    if yellow_point[0] < mid:
        yellow_point[0] = mid + (mid-yellow_point[0])
    if yellow_point[1] < mid:
        yellow_point[1] = mid + (mid-yellow_point[1])
    # 모든 계산이 끝난 후 left 값 mid 로 갱신
    left = mid
    # right 값은 기존 right 값과 총 접힌 부분의 길이 중 큰값을 right 값으로 갱신해준다.
    right = max(right,fold_length+mid)
# 위 과정을 파란점 노란점일 떄 반복 시행
if blue_point[0] != blue_point[1]:
    mid = (blue_point[0]+blue_point[1])/2
    fold_length = mid - left
    if yellow_point[0] < mid:
        yellow_point[0] = mid + (mid-yellow_point[0])
    if yellow_point[1] < mid:
        yellow_point[1] = mid + (mid-yellow_point[1])
    left = mid
    right = max(right,fold_length+mid)

if yellow_point[0] != yellow_point[1]:
    mid = (yellow_point[0]+yellow_point[1])/2
    fold_length = mid - left
    left = mid
    right = max(right,fold_length+mid)
# 최종 값에서 right 값과 left 차를 구한다.
print(f"{right-left:.1f}")