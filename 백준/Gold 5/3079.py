import sys

input = sys.stdin.readline

N, M = map(int,input().split())
# 출국 시간을 저장할 리스트
schedules = []

for _ in range(N):
    schedules.append(int(input()))

# 시작 값
left = 0
# 최대값 => 최대 인원수 * 최대 시간
right = 10**18

while left <= right:
    middle = (left+right)//2
    # 사람 수를 체크하는 변수
    count = 0
    # 최대 걸릴 수 있는 시간 나누기 입국 걸리는 시간 => 그 시간대에 받으면 되는 사람 수
    for schedule in schedules:
        count += middle // schedule
    # 어느 출국 시간에 사람을 몇명 받느냐에 따라서 count 값이 정해짐
    if count >= M:
        right = middle - 1
    else:
        left = middle + 1
print(left)