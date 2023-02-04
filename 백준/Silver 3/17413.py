word = input()
# 단어들을 문자열 합칠 변수
words = ""
# 거꾸로된 단어를 합칠 변수
reverse_word = ""
# <> 태그들을 담을 변수
tag = ""
# 태그인지 판단할 변수
check = 0
# 모든 값들들을 담을 리스트
word_list = []
# word 값들을 한개한개씩 반복문을통해 비교
for i in word:
    # i 값이 < 인 경우
    if i == "<":
        # words에 값이 들어있는경우
        if words != "":
            # revers_word에 words에 저장된 문자를 거꾸로 저장
            for j in words[::-1]:
                reverse_word += j
            # 역으로정렬한 word를 list에 추가
            word_list.append(reverse_word)
            # reverse_word 변수 초기화
            reverse_word = ""
            # words 변수도 초기화
            words = ""
        # tag변수에 < 추가
        tag += i
        # tag 가 시작이라고 알림
        check += 1
    # i 값이 > 로 닫는 태그일때
    elif i == ">":
        # tag에 i 더해준 후
        tag += i
        # word_list에 tag 단어 추가
        word_list.append(tag)
        # check를 통해 태그가 끝난걸 알려줌
        check -= 1
        # tag 변수 초기화
        tag = ""
    else:
        # 태그인지 아닌지 판별
        if check > 0:
            tag += i
        else:
        # i 가 공백인지 아닌지 판단
            if i == " ":
        # 공백일 경우 words에 저장한단어를 역순으로 저장
                for j in words[::-1]:
                    reverse_word += j
                word_list.append(reverse_word)
                word_list.append(i)
        # 변수 초기화
                reverse_word = ""
                words = ""
            else:
                words += i
# 맨마지막 단어는 추가되지 않았기때문에 별도로 추가
for k in words[::-1]:
    reverse_word += k
# 리스트에 저장된 값들 출력
for l in word_list:
    print(l,end="")
print(reverse_word)