R, C = map(int,input().split())

matrix = [ input() for _ in range(R) ]

word_list = []
# 가로 방향으로 반복하며 # 을 제외한 문자들을 정답 리스트에 저장
for i in range(R):
    word = ""
    for j in range(C):
        if matrix[i][j] == "#":
            # 막힌 부분에서 빈문자가 아니고 문자 길이가 1이 아닌 경우 추가 후 word 값 초기화
            if word != "":
                if len(word) > 1:
                    word_list.append(word)
            word = ""
        else:
            word += matrix[i][j]
    if word != "" and len(word) > 1:
        word_list.append(word)
# 세로 방향으로 반복하며 # 을 제외한 문자들을 리스트에 저장
for i in range(C):
    word = ""
    for j in range(R):
        if matrix[j][i] == "#":
            if word != "":
                if len(word) > 1:
                    word_list.append(word)
            word = ""
        else:
            word += matrix[j][i]
    if word != "" and len(word) > 1:
        word_list.append(word)

word_list.sort()

if word_list:
    print(word_list[0])