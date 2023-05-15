N = int(input())
# 문자를 저장할 리스트
word_list = []
# 문자열 저장
for _ in range(N):
    word_list.append(input())
# 최종적으로 사용할 리스트
total_list = []
# 리스트의 문자를 한개씩 반복해가는 반복문
for i in word_list:
    # 문자열의 모든 숫자를 번갈아가며 모든 경우의 수의 문자를 저장할 리스트
    middle_list = []
    # 문자열의 처음부터 끝까지 반복
    for j in range(len(i)):
        # 0~끝 1~끝 2~끝 이런식으로 더해나감
        word = i[j:] + i[:j]
        # 중간 리스트에 순회하는 문자를 저장
        middle_list.append(word)
    # 중간리스트를 정렬
    middle_list.sort()
    # 최종적인 리스트에 중간리스트 저장
    total_list.append(middle_list)
# 최종리스트를 set으로 중복처리를 해줘서 다른 문자열의 갯수를 파악
total_list = set(map(tuple,total_list))
print(len(total_list))