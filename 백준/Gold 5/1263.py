import sys

input = sys.stdin.readline

N = int(input())
# 일 시간 저장하는 리스트
work_lists = []

for _ in range(N):
    works = list(map(int,input().split()))
    work_lists.append(works)

# 끝나는 시간순으로 정렬
work_lists.sort(key = lambda x:x[1])
# 최소 시간 저장
min_value = sys.maxsize
# 현재 몇시간 일했는지 체크
current = 0
for i in work_lists:
    # 현재시간을 계속 더해나감
    current += i[0]
    # 임시 변수 check 를 통해서 몇시간 여유가 있는지를 확인
    check = i[1] - current
    # 만약 최소 시간보다 체크한 시간이 작은경우
    if check < min_value:
        # 최소 시간 갱신
        min_value = check
    # 최소 시간이 음수인경우 그 경우는 일을 처리할 수 없으므로 -1 출력
    if min_value < 0:
        print(-1)
        break
else:
    print(min_value)