# 인풋 처리
import sys
# 많은 인풋
input = sys.stdin.readline

N, K = map(int,input().split())
# 랜선 길이
num_list = []
# 최대값 최소값 설정
right = 2**31 - 1
left = 1

for _ in range(N):
    num_list.append(int(input()))
# 이분 탐색
while left <= right:
    # 중앙값 설정
    middle = (left+right) // 2
    # 개수 체크
    cnt = 0
    # 중앙 값으로 랜선을 자른 개수 체크
    for num in num_list:
        cnt += (num // middle)
    # 만약 개수가 목표인 K 보다 작으면 right 는 middle -1 외의 경우 left 는 middle + 1
    if cnt < K:
        right = middle - 1
    elif cnt >= K:
        left = middle + 1

print(right)