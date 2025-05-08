from collections import deque
# 단어 길이 체크
word = input()
word_length = len(word)
# 뒤집을 리스트 생성
stack = deque([word[0]])
# 단어 끝까지 탐색하며
for i in range(1,word_length):
    # 단어가 이전의 단어보다 큰 경우 그대로 추가
    if word[i] >= stack[-1]:
        stack.append(word[i])
    # 외의 경우 처음 단어랑 비교해서 작으면 그 앞에 추가 아닌경우 맨뒤에 추가
    else:
        if word[i] <= stack[0]:
            stack.appendleft(word[i])
        else:
            stack.append(word[i])
# join을 통한 정답출력
print("".join(stack))