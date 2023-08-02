# deque 선언
from collections import deque

N, M = map(int,input().split())
# 찾고자 하는 숫자 리스트
answer_list = list(map(int,input().split()))
# 초기 인덱스값
index = 0
# deque 선언
deque_list = deque()
# deque에 1 ~ N 까지 값추가
for i in range(1,N+1):
    deque_list.append(i)
cnt = 0
# 인덱스 값이 찾고자 하는 숫자의 개수 전 까지 반복
while index != M:
    # check_num 에 찾고자 하는 숫자의 값들을 한개씩 대입
    check_num = answer_list[index]
    # 0번째 인덱스 값이 찾는 값이 아닌 경우
    if check_num != deque_list[0]:
        # 찾고자 하는 숫자가 deque_list에 가운데 인덱스를 기준으로 왼쪽인지 오른쪽인지 판단.
        if N//2 >= deque_list.index(check_num):
            # 중앙에서 왼쪽인 경우 리스트를 -1 방향으로 계속 돌리며 cnt 값 증가
            while deque_list[0] != check_num:
                deque_list.rotate(-1)
                cnt += 1
        elif N//2 < deque_list.index(check_num):
            # 찾고자 하는 숫자가 deque_list에 가운데 인덱스를 기준으로 오른쪽인 경우 리스트를 +1 방향으로 계속 돌리며 cnt 값 증가
            while deque_list[0] != check_num:
                deque_list.rotate(1)
                cnt += 1
    # deque_list 에서 젤 왼쪽값 제거 후 N 값 -1
    deque_list.popleft()
    N -= 1
    index += 1
print(cnt)

# matrix = [[3, 3, 5, 3, 1], [2, 2, 4, 2, 6], [4, 9, 2, 3, 4], [1, 1, 1, 1, 1], [3, 3, 5, 9, 2]]
# total_matrix = [ [0] * 5 for _ in range(5) ]
# dx = [-1, 1, -1 ,1]
# dy = [-1, -1, 1, 1]

# max_value = 0
# max_index = [0, 0]

# for i in range(5):
#     for j in range(5):
#         for k in range(4):
#             x = i + dy[k]
#             y = j + dx[k]
#             if (0 <= x < 5) and (0 <= y < 5):
#                 total_matrix[i][j] += matrix[x][y]
#         if total_matrix[i][j] > max_value:
#             max_value = total_matrix[i][j]
#             max_index[0] = i
#             max_index[1] = j

# print(*max_index)