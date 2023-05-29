# 키를 담을 변수
keyword = input()
# 암호문을 담을 변수
texts = input()
# 키의 길이
keyword_length = len(keyword)
# 암호문의 길이
texts_length = len(texts)
# 암호문의 길이에서 키의 길이를 나눠준 변수 => 리스트 길이때문에
answer_length = texts_length//keyword_length
# 암호문을 길이에 맞도록 잘라서 담을 리스트
texts_list = []
# 들어온 키 값을 인덱스 번호와 함께 저장할 리스트
check_list = []
# 정렬된 순서를 저장할 리스트
answer_list= []
# 인덱스 번호를 저장할 변수
cnt = 0
# 들어온 키값을 인덱스 번호와 리스트에 튜플 형태로 저장함
for i in keyword:
    check_list.append((i,cnt))
    cnt += 1
# 키값을 정렬
check_list.sort()

# 인덱스 순서를 담을 변수
cnt = 0
# sort를 사용하였기 때문에 기존의 문자들의 위치를 모르기 때문에 cnt 변수를 사용하여 몇번위치부터 순서대로 정렬됐는지 answer_list 에 추가해준다.
for i in range(keyword_length):
    for j in range(keyword_length):
        if check_list[j][1] == cnt:
            answer_list.append(j)
            cnt += 1
            break
# answer_length 간격마다 문자를 잘라서 리스트에 저장해준다.
for i in range(keyword_length):
    check = i*answer_length
    texts_list.append(texts[check:check+answer_length])
# 정답을 출력할 변수
answer = ""
# answer_list 에 저장된 인덱스번호 순서대로 answer에 값을 더해준다
for j in range(answer_length):
    for i in range(len(texts_list)):
        answer += texts_list[answer_list[i]][j]

print(answer)