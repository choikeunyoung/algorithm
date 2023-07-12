from collections import deque

N = int(input())
# 카드 리스트를 deque로 선언
card_list = deque()
# 1~N 까지 카드 리스트 생성
for i in range(1,N+1):
    card_list.append(i)
# card의 길이 변수로 생성
card_length = len(card_list)
# 카드 길이가 1일때 까지 반복
while card_length > 1:
    # 카드 길이의 왼쪽 값을 뽑아옴
    card_list.popleft()
    # 카드에서 한번더 왼쪽 값을 뽑아서 변수에 저장
    check = card_list.popleft()
    # 뽑은 값을 오른쪽에 추가
    card_list.append(check)
    # 한번 시행했으므로 카드 길이 -1 해줌
    card_length -= 1
print(card_list[0])