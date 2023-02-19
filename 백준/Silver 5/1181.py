N = int(input())
# 문자 담을 리스트 생성
char_list = []
# 리스트 들어오면서 값 저장
for _ in range(N):
    # 문자 저장
    word = input()
    # 문자 길이저장
    word_len = len(word)
    # 길이, 문자 형태로 리스트 저장
    char_list.append((word_len, word))
# 리스트 중복제거 후 다시 리스트 형태로 반환
char_list = list(set(char_list))
# 리스트를 lambda 함수를 사용하여 길이순으로 정렬하고 길이가 같은경우 문자로 정렬
char_list.sort(key = lambda x:(x[0],x[1]))
for i in range(len(char_list)):
    print(char_list[i][1])