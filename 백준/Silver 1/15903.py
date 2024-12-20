import heapq
# n,m 인풋값 받기
n,m = map(int,input().split())
# 리스트 우선순위 큐로 변환
num_list = list(map(int,input().split()))
heapq.heapify(num_list)
# 첫째 값, 둘째 값 우선순위 큐 추출
for i in range(m):
    first = heapq.heappop(num_list)
    second = heapq.heappop(num_list)
    # 덮어씌울 값 우선순위 큐에 추가
    next = first + second
    heapq.heappush(num_list,next)
    heapq.heappush(num_list,next)

print(sum(num_list))