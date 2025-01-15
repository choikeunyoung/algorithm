import sys
# 많은 인풋 처리
input = sys.stdin.readline
# N 과 M 인풋
N, M = map(int,input().split())
# 점들 리스트
num_list = list(map(int,input().split()))
# 점들 정렬
num_list.sort()
# M 선분 횟수만큼 반복
for _ in range(M):
    # 시작점 끝점 받기
    start,end = map(int,input().split())
    # 시작점과 끝점이 범위내에 없는 경우 연산 제외
    if start > num_list[-1] or end < num_list[0]:
        print(0)
        continue
    # lower bound 부분에서 인덱스 체크
    left_point = 0
    # upper bound 부분에서 인덱스 체크
    right_point = 0
    # 시작점 끝점 설정
    left = 0
    right = N-1
    # 이분 탐색 진행하며 lower bound 체크
    while left <= right:
        middle = (left+right)//2

        if num_list[middle] >= start:
            left_point = middle
            right = middle - 1
        else:
            left = middle + 1
    # 시작점 끝점 초기화
    left = 0
    right = N - 1
    # upper bound 체크
    while left <= right:
        middle = (left+right)//2

        if num_list[middle] <= end:
            right_point = middle
            left = middle + 1
        else:
            right = middle - 1
    # 인덱스 이므로 upper bound - lower bound + 1 해줌
    print(right_point - left_point + 1)