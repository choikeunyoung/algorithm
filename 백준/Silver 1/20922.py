N, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_cnt = [0] * 100001
# 시작
left = 0
# 끝
right = 0
# 최대 길이 체크
max_length = 0
# N까지 반복문 진행
while right < N:
    # num_list 의 값 나올 때마다 1씩 증가
    num_cnt[num_list[right]] += 1
    # K 개보다 더 많이 나오는 경우
    if num_cnt[num_list[right]] > K:
        # max_length 값 갱신
        if max_length < right - left:
            max_length = right - left
        # num_cnt에서 num_list의 값이 K 보다 작을때까지 left 값증가하며 반복
        while num_cnt[num_list[right]] > K:
            num_cnt[num_list[left]] -= 1
            left += 1
    right += 1
# 맨 마지막 리스트 순회에서 값 갱신
else:
    if max_length < right - left:
        max_length = right - left
print(max_length)
