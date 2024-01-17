def solution(friends, gifts):
    # 선물 리스트
    friend_dict = {}
    # 선물을 받은 개수 체크
    present_cnt = {}
    # 친구들 리스트를 순환하며 딕셔너리에 인원들 넣음
    for friend in friends:
        friend_dict[friend] = {}
        # 인원들 리스트 돌며 누구에게 선물 줬는지 체크
        for person in friends:
            friend_dict[friend][person] = 0
        # 선물 받은 개수 체크
        present_cnt[friend] = 0
    # 누구에게 선물 줬는지 리스트로 split
    for gift in gifts:
        gift = gift.split()
        # 선물을 주고 받은 값들 체크
        friend_dict[gift[0]][gift[1]] += 1
        friend_dict[gift[1]][gift[0]] -= 1
        present_cnt[gift[1]] -= 1
        present_cnt[gift[0]] += 1
    # 최대 선물 개수 체크
    max_present = 0
    # key, value 쌍으로 아이템 체크
    for k,v in friend_dict.items():
        # 선물 받은 개수 체크
        cnt = 0
        # value 딕셔너리에서 key, value 뽑아냄
        for key, value in v.items():
            # k 값이 key랑 같은 값이 아닌 경우
            if key != k:
                # value 가 0인 경우는 선물을 주고받지 않은 경우 혹은 같은 선물을 준 경우
                if value == 0:
                    # 둘의 행복지수 비교하여 크면 cnt 증가
                    if present_cnt[k] > present_cnt[key]:
                        cnt += 1
                # 외의 경우 선물을 더 많이 준 경우 받을 선물 증가
                elif value > 0:
                    cnt += 1
        # 최대 선물의 개수와 받은 선물 비교 후 값 갱신
        if cnt > max_present:
            max_present = cnt    
                    
    answer = max_present
    return answer