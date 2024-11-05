# 이진 탐색을 통한 들어갈 인덱스 찾기
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
# 숫자 리스트
num_list = list(map(int,input().split()))
# LIS 길이 1로 설정
dp_length = 1
# 초기 값으로 리스트 0번 인덱스값
dp = [num_list[0]]
# 최장 길이 수열이 몇인지 체크할 리스트
dp_array = [0]

# 반복문 진행
for i in range(1,N):
    # dp에 저장된 끝값이 인풋보다 더 작은경우
    if dp[-1] < num_list[i]:
        # dp 길이 1 증가
        dp_length += 1
        # 끝 값 추가
        dp.append(num_list[i])
        # 경로 리스트에 최대 길이 -1 인덱스 저장
        dp_array.append(dp_length - 1)
    else:
        # 끝값보다 작은경우 들어갈 인덱스 찾기
        next_index = binary_search(dp_length,num_list[i])
        # 들어가는 인덱스 자리에 num_list[i] 값 대입
        dp[next_index] = num_list[i]
        # LIS 인덱스에 들어갈 위치 저장
        dp_array.append(next_index)

ans = []
# 끝에서 반복문 진행 하며 LIS 길이와 array에 저장된 값이 같을때 정답 리스트에 저장 후 길이 -1
for i in range(N-1,-1,-1):
    if dp_array[i] == dp_length-1:
        ans.append(num_list[i])
        dp_length -= 1
# 저장된 리스트 뒤집고 길이와 전부 출력
ans.reverse()
print(len(ans))
print(*ans)