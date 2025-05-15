import sys

input = sys.stdin.readline

N = int(input())
# 숫자 리스트
num_list = []

for _ in range(N):
    num_list.append(int(input()))
# 숫자 정렬
num_list.sort()
# 중복 수 제거
two_set = set()
# 리스트 중 두 수를 골라 나올 수 있는 모든 합의 경우의 수 저장
for i in range(N):
    for j in range(i,N):
        two_set.add(num_list[i]+num_list[j])
# 기존 리스트 역순 탐색
for num in reversed(num_list):
    # 0번 인덱스부터 탐색
    for i in range(N):
        # 기존 리스트 역순 탐색 - 현재 인덱스 값이 두 수를 더한 set 에 존재할 경우 리스트 값 출력 후 종료
        if num - num_list[i] in two_set:
            print(num)
            exit()
