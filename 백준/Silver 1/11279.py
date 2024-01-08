import heapq
import sys

input = sys.stdin.readline

num_list = []

N = int(input())

for _ in range(N):
    # 인풋 값 체크
    input_num = int(input())
    # 인풋 값이 0 인 경우
    if input_num == 0:
        # num_list 값이 존재하는지 체크
        if num_list:
            # 값이 있는 경우 heappop을 사용하여 최소값 출력하며 - 붙이면 최대값이 됨
            print(-heapq.heappop(num_list))
        else:
            # 외의 경우 0 출력
            print(0)
    else:
        # 값을 넣을때 최대값을 뽑기위해 -를 붙여서 값을 너어줌
        heapq.heappush(num_list, -input_num)
