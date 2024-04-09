N = int(input())
# 단어 저장
word_list = []
# 단어 길이와 문자로 저장
for _ in range(N):
    word = input()
    word_list.append([len(word),word])
# 길이로 정렬 진행
word_list.sort(key= lambda x : (x[0], x[1]))
# 부분 집합의 개수 체크
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        # 접두사로 시작하는지 판단
        if (word_list[j][1][:word_list[i][0]] == word_list[i][1]):
            cnt += 1
            break
# N 에서 부분집합 개수 제거
print(N-cnt)