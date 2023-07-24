# 인풋 값
word = input()
# 인풋 값의 길이
word_length = len(word)
# 정답을 출력할 Set
set_list = set()
# 리스트 길이 만큼 반복문 시행
for i in range(word_length):
    # 리스트 길이만큼 반복문을 시행하지만 시작값이 i+1 부터 시작
    for j in range(i+1,word_length+1):
        # 단어를 슬라이싱을 통해서 set에 추가
        set_list.add(word[i:j])
# 중복제거가 된 값들 길이 출력
print(len(set_list))