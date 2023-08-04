word = input()
# 단어 길이
word_length = len(word)
# 단어랑 단어의 역순이 같으면 팰린드롬 이므로 길이 출력
if word == word[::-1]:
    print(word_length)
# 다른 경우
else:
    # 단어의 0번 인덱스부터 끝까지 탐색하며
    for i in range(word_length):
        # check_word 의 초기값으로 input 단어 입력
        check_word = word
        # 이후 단어의 i 번인덱스까지 문자를 역순으로 더함
        check_word += word[:i+1][::-1]
        # 더한 문자가 팰린드롬인지 판단
        if check_word == check_word[::-1]:
            print(len(check_word))
            break