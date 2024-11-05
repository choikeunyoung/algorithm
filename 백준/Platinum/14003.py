# 이진 탐색
def binary_search(right,value):
    left = 0
    middle = 0
    while left < right:
        middle = (left + right) // 2
        if dp[middle] < value:
            left = middle + 1
        else:
            right = middle
    return right

N = int(input())

num_list = list(map(int,input().split()))
# DP 리스트 길이 1
dp_length = 1
# 초기값 0번 값
dp = [num_list[0]]
# 각 숫자 인덱스별 길이가 몇인지 체크
dp_array = [0]
# 반복문 1 ~ N 까지
for i in range(1,N):
    # 끝의 값이 들어온 num_list[i] 값보다 작은 경우
    if dp[-1] < num_list[i]:
        # dp 길이 체크 변수 1 증가
        dp_length += 1
        # dp 에 들어온 값 추가
        dp.append(num_list[i])
        # 각 인덱스 별 최대 길이 추가
        dp_array.append(dp_length - 1)
    else:
        # 이진 탐색으로 들어갈 인덱스 반환
        next_index = binary_search(dp_length,num_list[i])
        # 이진 탐색으로 구한 인덱스에 들어온 num_list 값 갱신
        dp[next_index] = num_list[i]
        # 인덱스 별 최대 길이 체크하는 곳에 인덱스 추가
        dp_array.append(next_index)

ans = []

for i in range(N-1,-1,-1):
    if dp_array[i] == dp_length-1:
        ans.append(num_list[i])
        dp_length -= 1
ans.reverse()
print(len(ans))
print(*ans)