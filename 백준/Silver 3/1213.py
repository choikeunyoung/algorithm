word = input()
word_length = len(word)
# 들어온 길이가 1인 경우 무조건 word 출력
if word_length == 1:
    print(word)
# 2인 경우 0번 인덱스와 1번 인덱스가 다른지 확인
elif word_length == 2:
    if word[0] == word[1]:
        print(word)
    else:
        print("I'm Sorry Hansoo")
# 그 외의 경우
else:
    # 인풋값을 우선 정렬
    sorted_word = sorted(word)
    # 딕셔너리 생성 => 갯수 세기 위해
    sorted_dict = {}
    for i in sorted_word:
        if i in sorted_dict:
            sorted_dict[i] += 1
        else:
            sorted_dict[i] = 1
    
    if word_length %2 == 0:
        answer = ""
        for k,v in sorted_dict.items():
            if v % 2 == 1:
                print("I'm Sorry Hansoo")
                answer = ""
                break
            else:
                if v//2 == 0:
                    answer = answer + k
                else:
                    answer = answer + k*(v//2)
        if answer != "":
            print(answer+answer[::-1])
    else:
        answer = ""
        cnt = 0
        min_cnt = min(sorted_dict.values())
        for k,v in sorted_dict.items():
            if v % 2 == 1:
                cnt += 1
                check = k
                sorted_dict[k] -= 1
                if sorted_dict[k] == 0:
                    pass
                else:
                    answer = answer + k*(sorted_dict[k]//2)
            else:
                if v//2 == 0:
                    answer = answer + k
                else:
                    answer = answer + k*(v//2)
            if cnt >= 2:
                print("I'm Sorry Hansoo")
                answer = ""
                check = ""
                break
        if answer != "":
            print(answer+check+answer[::-1])