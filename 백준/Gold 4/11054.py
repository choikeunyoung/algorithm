N = int(input())
# 인풋
num_list = list(map(int,input().split()))
# 리버스 인풋
reverse_list = num_list[::-1]
# LIS 증가
increase_cnt = [0] * N
# LIS 감소
decrease_cnt = [0] * N
# 초기값 선언
increase_cnt[0] = 1
decrease_cnt[0] = 1
# LIS 증가 로직
for i in range(N):
    increase_cnt[i] = 1
    for j in range(i):
        if num_list[j] < num_list[i]:
            increase_cnt[i] = max(increase_cnt[j]+1, increase_cnt[i])
# LIS 감소 로직
for i in range(N):
    decrease_cnt[i] = 1
    for j in range(i):
        if reverse_list[j] < reverse_list[i]:
            decrease_cnt[i] = max(decrease_cnt[i], decrease_cnt[j]+1)
# 최대값
max_value = 0
# i 번 인덱스일떄 증가 감소 값 체크
for i in range(N):
    total = increase_cnt[i] + decrease_cnt[N-i-1]
    # 최대 값 갱신
    if total > max_value:
        max_value = total
# 최대값 - 1 같은 위치의 수는 중복되기 때문에
print(max_value - 1)