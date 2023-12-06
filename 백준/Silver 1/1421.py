import sys

input = sys.stdin.readline

N, C, W = map(int, input().split())
# 나무를 담을 리스트
wood_list = []

for _ in range(N):
    wood_list.append(int(input()))
# 나무를 작은값부터 큰수로 오름차순 정렬
wood_list.sort()

max_wood = 0
# 1부터 최대 나무길이까지 반복
for i in range(1, wood_list[-1] + 1):
    # 현재 가격변수 선언
    current_value = 0
    # 나무 리스트를 반복하며
    for j in wood_list:
        # 자르는 길이가 나무보다 작은경우
        if j > i:
            # 나무 자른 횟수체크
            cut_cnt = j // i
            # 길이가 남았는지 확인할 변수
            r = j % i
            # 나머지가 없으면 자르는 횟수 -1
            if r == 0:
                cut_cnt -= 1
            # 이득값 계산해는 식 몫 * W * 현재 나무 길이 - 자른 횟수 * 자르는 비용
            profit = ((j // i) * W * i) - (cut_cnt * C)
            # 이득값이 음수면 패스
            if profit < 0:
                continue
            # profit 을 현재 값에 더해나감
            current_value += profit
        # 그냥 j와 i가 같으면 자를필요없이 값 더해줌
        elif j == i:
            current_value += i * W
    # 최대값 비교
    if current_value > max_wood:
        max_wood = current_value
print(max_wood)
