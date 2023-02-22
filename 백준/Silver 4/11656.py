word = input()
# 문자를 담을 리스트 생성
word_list = []
# 문자 길이만큼 슬라이스
for i in range(len(word)):
    word_list.append(word[i:])

# 문자열 정렬
word_list.sort()
# 출력
for i in word_list:
    print(i)