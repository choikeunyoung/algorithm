import heapq
import sys
# 많은 인풋 처리
input = sys.stdin.readline

N = int(input())
# 리스트 생성
num_list = []

for _ in range(N):
    # num 값 인풋으로 받음
    num = int(input())
    if num == 0:
        # num_list 가 비어있으면
        if not num_list:
            # 0 출력
            print(0)
        else:
            # 외의 경우 우선순위 큐 값 출력
            print(heapq.heappop(num_list))
    else:
        # 우선순위 큐에 값 푸쉬
        heapq.heappush(num_list,num)