import heapq
# 인풋
N = int(input())
# 리스트 저장할 리스트
num_list = []
# 강의실 번호 N 은 필요없으므로 시작과 끝값 리스트 저장
for _ in range(N):
    N, S, E = map(int,input().split())
    num_list.append([S,E])
# 0번 인덱스 기준으로 정렬
num_list.sort(key= lambda x:x[0])
# 정답을 출력할 리스트
answer = []
# 리스트를 순회하며
for nums in num_list:
    # 리스트 값이 있는 경우
    if answer:
        # 시작 시간이 answer 에 저장된 시간보다 작은 경우 새롭게 추가
        if nums[0] < answer[0]:
            heapq.heappush(answer,nums[1])
        # 만약 크거나 같은 경우 answer에 값을 뽑고 다시 추가
        else:
            heapq.heappop(answer)
            heapq.heappush(answer,nums[1])
    # 리스트가 비었을 경우 끝값 추가
    else:
        heapq.heappush(answer,nums[1])
# 길이 추가
print(len(answer))