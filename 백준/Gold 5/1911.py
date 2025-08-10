import sys

input = sys.stdin.readline

N, L = map(int,input().split())

lists = []
# 웅덩이 개수
for _ in range(N):
    start, end = map(int,input().split())
    lists.append((start,end))
# 웅덩이 정렬
lists.sort()
# 널빤지 개수
cnt = 0
# 현재 마지막 위치
current_end = 0
# 웅덩이 시작점 끝점
for s, e in lists:
    # 현재 위치가 시작점보다 낮으면 시작점 갱신
    if current_end < s:
        current_end = s
    # 현재 위치가 끝보다 크면 다음 리스트
    if current_end >= e:
        continue
    # 현재 덮어야할 길이
    length = e - current_end
    # 널빤지 개수 체크
    next = (length + L - 1) // L
    # 널빤지 개수 증가
    cnt += next
    # 이후 끝 길이 체크
    current_end += (next * L)

print(cnt)