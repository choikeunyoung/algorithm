def backtracking(current):
    global cnt
    # 현재 값이 시작인경우 ans 리스트에 값을 한개씩 추가해 나가며 방문했는지 체크
    if current == 0:
        for i in range(word_length):
            ans.append(word[i])
            visited[i] = True
            backtracking(current + 1)
            visited[i] = False
            ans.pop()
    else:
        # 만약 리스트 길이와 같으면 리스트를 set에 저장
        if current == word_length:
            check = "".join(ans)
            answer_list.add(check)
            return
        # 0부터 리스트 길이까지 반복문을 진행하며 방문했는지 이전값이랑 같은지 체크 조건에 맞으면 백트래킹
        for i in range(word_length):
            if word[i] != ans[-1] and not visited[i]:
                ans.append(word[i])
                visited[i] = True
                backtracking(current + 1)
                visited[i] = False
                ans.pop()


word = input()
word_dict = {}
ans = []
answer_list = set()
cnt = 0
word_length = len(word)
visited = [False] * word_length
current = 0
backtracking(current)
print(len(answer_list))
