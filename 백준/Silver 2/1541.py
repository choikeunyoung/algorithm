# -가 들어있는 부분을 기준으로 인풋값을 짜른다.
word = list(map(str,input().split("-")))

answer_list = []
# word의 길이만큼 반복문을 진행하는데
for i in range(len(word)):
    # 만약 word[i]에 + 연산자가 들어있는 경우
    if "+" in word[i]:
        # 이 값들도 + 를 기준으로 정수로 변환하여 리스트로 잘라준다.
        hap_list = list(map(int,word[i].split("+")))
        # 이후 이 값들을 합한 값을 word[i]에 넣어준다.
        word[i] = sum(hap_list)
# 정답을 출력할 변수
answer = 0
# 만약 word 가 - 연산자가 있는 경우 리스트는 2개 이상으로 나뉜다.
if len(word) > 1:
    # word의 길이만큼 반복을 하며
    for j in range(len(word)):
        # 처음 인덱스 값은 무조건 더해준 후
        if j == 0:
            answer += int(word[j])
        # 이후 인덱스는 answer 변수에 값을 계속해서 뺴준다.
        else:
            answer -= int(word[j])
    print(answer)
# word에 - 연산자가 없는 경우 0 번 인덱스 출력
else:
    print(word[0])