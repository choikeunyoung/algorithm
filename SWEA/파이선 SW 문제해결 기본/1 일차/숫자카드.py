T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cards = input()
    card_dict = {}
    # card의 숫자들을 딕셔너리에 값이 있으면 +1 없으면 1로 저장
    for card in cards:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    # 딕셔너리 값들중 최대값 찾기
    max_card = max(card_dict.values())
    # 정답을 출력할 리스트
    answer_list = []
    # 딕셔너리 key, value를 순회하며 value 값이 max 값과 같은경우 answer_list에 추가
    for k,v in card_dict.items():
        if v == max_card:
            answer_list.append(k)
    # answer_list 가 1보다 큰 경우
    if len(answer_list) > 1:
        # answer_list 의 max 값과 max_card 출력
        print(f"#{tc} {max(answer_list)} {max_card}")
        # anwer_list에 들어있는 0번 인덱스 값과 max_card 출력
    else:
        print(f"#{tc} {answer_list[0]} {max_card}")