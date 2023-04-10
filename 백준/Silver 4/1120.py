word_1,word_2 = input().split()
# 첫번째 단어와 두번째 단어의 길이가 같은지 아닌지 판단
if len(word_1) == len(word_2):
    cnt = 0
    # 길이가 같은경우 한개의 길이를 반복문을통해서 탐색
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            # 다른경우 cnt 라는 변수를 +1 해줌
            cnt += 1
    # 다른 부분의 갯수를 출력
    print(cnt)
# 단어의 길이가 다른경우
else:
    # 첫번째 단어의 길이와 두번째 단어의 길이를 각각 변수에 저장
    word_1_length = len(word_1)
    word_2_length = len(word_2)
    # 정답 리스트에 값출력
    ans_list = []
    # 두번째 단어와 첫번째 단어의 길이차 +1 범위까지 반복분 시행
    for j in range(word_2_length-word_1_length+1):
        # cnt 변수에 0 을 저장
        cnt = 0
        # 첫번째 단어의 길이만큼 반복문 시행
        for k in range(word_1_length):
            # 첫번째 단어와 두번째단어의 시작값을 변경해가며 값을 비교
            if word_1[k] != word_2[j+k]:
                # 다른 경우 갯수를 체크
                cnt += 1
        # 정답 리스트에 반복문을 통한 갯수를 체크한 변수 추가
        ans_list.append(cnt)
    # 그 중 제일 작은 값의 변수를 추가
    print(min(ans_list))