import sys

input = sys.stdin.readline

N = int(input())

num_list = []
# 숫자 리스트 추가
for _ in range(N):
    num_list.append(int(input()))
# LIS 알고리즘 적용할 리스트
long_length = [0] * N
# LIS 알고리즘
for i in range(N):
    # i 번 값 1로 초기화
    long_length[i] = 1
    # 0번 인덱스부터 i 번 인덱스까지 반복문진행
    for j in range(0,i):
        # i 번 인덱스 값보다 작은경우
        if num_list[j] < num_list[i]:
            # 현재 i 인덱스에 기존의 i 인덱스 값 혹은 값이 작은 j 번 인덱스 +1 한 값중 맥스값 추가
            long_length[i] = max(long_length[i], long_length[j]+1)
# 개수 N 에서 LIS 적용한 max 값 빼줌
print(N-max(long_length))