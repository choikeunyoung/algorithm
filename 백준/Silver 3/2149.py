keyword = input()
texts = input()
keyword_length = len(keyword)
texts_length = len(texts)
answer_length = texts_length//keyword_length
texts_list = []
check_list = []
cnt = 0
for i in keyword:
    check_list.append((i,cnt))
    cnt += 1
check_list.sort()

for i in range(keyword_length):
    check = i*answer_length
    texts_list.append(texts[check:check+answer_length])

answer = ""

for j in range(keyword_length):
    for i in range(len(texts_list)):
        answer += texts_list[i][check_list[j][1]]

print(texts_list,texts_length)