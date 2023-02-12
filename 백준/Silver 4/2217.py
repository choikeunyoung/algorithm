N = int(input())
# 로프 리스트 생성
lope_list = []

for _ in range(N):
    lope_list.append(int(input()))

# 로프 리스트를 큰순으로 정렬함 내림차순(큰거=>작은거)
lope_list.sort(reverse=True)

# check 라는 변수로 시작할때 값을 설정
check = 0
# max_weight로 값 설정
max_weight = 0

for i in range(N):
# 만약 시작하는 값이면
    if check == 0:
# min_num 에 리스트 처음 요소를 넣어준다.
        min_num = lope_list[0]
# check 라는 변수에 값을 넣어 처음이 아닌 것을 나타냄
        check += 1
# max_weight 에 min_num * i 를 해준다. => min_num * i 해주는 이유는 로프의 개수에 따라서 받는 하중이 달라지기 때문이다.
        max_weight = min_num * 1
    else:
# min_num값이 lope_list 리스트를 순회하며 최소값인지 판단
        if min_num > lope_list[i]:
            min_num = lope_list[i]
# min_num값의 최대 중량이 max_weight 보다 큰 경우 max_weight 값에 넣어줌
        if max_weight < min_num*(i+1):
            max_weight = min_num*(i+1)
print(max_weight)