# input 값
N, S = map(int,input().split())
# 숫자 리스트
num_list = list(map(int,input().split()))
# 정렬
num_list.sort()
# 딕셔너리를 통해서 몇개 나왔는지 체크
answer_dict = {}
# 왼쪽 부분 합
left_sum = []
# 오른쪽 부분 합
right_sum = []
# 왼쪽 부분 합 구하는 로직
for i in range(N//2):
    left_length = len(left_sum)
    for j in range(left_length):
        left_sum.append(left_sum[j]+num_list[i])
    left_sum.append(num_list[i])
# 오른쪽 부분 합 구하는 로직
for i in range(N//2,N):
    right_length = len(right_sum)
    for j in range(right_length):
        right_sum.append(right_sum[j]+num_list[i])
    right_sum.append(num_list[i])
# 총 몇개의 S 가 나오는지 체크
cnt = 0

# 왼쪽 리스트를 순회하며 S인 경우 체크 및 딕셔너리에 왼쪽 리스트 값 추가
for i in left_sum:
    if i == S:
        cnt += 1
    if i in answer_dict:
        answer_dict[i] += 1
    else:
        answer_dict[i] = 1
# 오른쪽 리스트를 순회하며 S인 경우 체크
for i in right_sum:
    if i == S:
        cnt += 1
# 왼쪽 리스트 정렬, 오른쪽 리스트 정렬
left_sum.sort()
right_sum.sort()
# 왼쪽 리스트 길이 체크, 시작 인덱스, 오른쪽 리스트 시작 값 선택
left_length = len(left_sum)
left_index = 0
right_index = len(right_sum)-1
# 왼쪽 리스트 인덱스 값이 길이보다 작고 오른쪽 인덱스가 0 보다 크거나 같을때 까지
while left_index < left_length and right_index > -1:
    # 왼쪽 리스트 값 + 오른쪽 리스트 값이 S 보다 작으면 왼쪽 리스트 인덱스 +1
    if left_sum[left_index] + right_sum[right_index] < S:
        left_index += 1
    # 왼쪽 리스트 값 + 오른쪽 리스트 값이 S 보다 큰 경우 오른쪽 리스트 인덱스 -1
    elif left_sum[left_index] + right_sum[right_index] > S:
        right_index -= 1
    # 외의 경우 같을 때
    else:
        # cnt 값에 딕셔너리에 저장된 왼쪽 리스트 값의 개수를 증가
        cnt += answer_dict[S - right_sum[right_index]]
        # 오른쪽 리스트 크기가 더 크기 떄문에 -1
        right_index -= 1
print(cnt)