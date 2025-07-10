N, M = map(int,input().split())

num_list = list(map(int,input().split()))
# 마이너스 리스트
minus_list = []
# 플러스 리스트
plus_list = []
# 최대 거리 저장
max_value = -(10**6)
# 마이너스 리스트와 플러스 리스트, 최대 거리 저장
for num in num_list:
    if num < 0:
        minus_list.append(num)
    else:
        plus_list.append(num)

    if max_value < abs(num):
        max_value = abs(num)

# 두 리스트 정렬
minus_list.sort()
plus_list.sort(reverse=True)
# 정답 출력할 변수
answer = 0
# 가장 먼 거리부터 M개의 책을 들고가기 때문에 인덱스 증가 M 으로 설정
for i in range(0,len(minus_list),M):
    answer += (minus_list[i]*-2)

for i in range(0,len(plus_list),M):
    answer += (plus_list[i]*2)
# 왕복 최대거리에서 최대로 갈 수 있는 거리 빼줌
print(answer-max_value)