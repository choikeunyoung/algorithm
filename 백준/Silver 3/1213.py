word = input()
word_length = len(word)
# 들어온 길이가 1인 경우 무조건 word 출력
if word_length == 1:
    print(word)
# 2인 경우 0번 인덱스와 1번 인덱스가 다른지 확인
elif word_length == 2:
    if word[0] == word[1]:
        print(word)
    else:
        print("I'm Sorry Hansoo")
# 그 외의 경우
else:
    # 인풋값을 우선 정렬
    sorted_word = sorted(word)
    # 딕셔너리 생성 => 갯수 세기 위해
    sorted_dict = {}
    # 딕셔너리에 값을 넣으며 갯수를 세는 중
    for i in sorted_word:
        if i in sorted_dict:
            sorted_dict[i] += 1
        else:
            sorted_dict[i] = 1
    # 만약 길이가 짝수인 경우
    if word_length %2 == 0:
        answer = ""
        # 딕셔너리 key, value 를 순환하며
        for k,v in sorted_dict.items():
            # value 값이 홀수 인 경우 대칭이 될 수 없다.
            if v % 2 == 1:
                print("I'm Sorry Hansoo")
                answer = ""
                break
            # 짝수인 경우
            else:
                # value값이 1,1 인경우 1번 나왔기 때문에 answer에 k 한번만 더해준다.
                if v//2 == 0:
                    answer = answer + k
                # 그 외의 경우 몫만큼 곱한걸 더해준다.
                else:
                    answer = answer + k*(v//2)
        # 만약 변수가 공백이면 0부터 끝까지와 끝에서부터 0까지를 더해서 출력해준다.
        if answer != "":
            print(answer+answer[::-1])
    # 홀수인 경우
    else:
        answer = ""
        # 홀수인 경우 짝수인 경우와는 다르게 홀수의 갯수를 체크해줘야 하기 때문에 변수를 넣어준다.
        cnt = 0
        # 짝수일때와 마찬가지로 반복문 시행
        for k,v in sorted_dict.items():
            # 홀수의 경우 홀수일때 홀수의 갯수를 체크해줘야 한다.
            if v % 2 == 1:
                cnt += 1
                # 홀수일때 check 라는 변수에 key 값을 넣어준다
                check = k
                # 이제 딕셔너리의 value 값을 -1 해줘서 짝수로 바꿔준다.
                sorted_dict[k] -= 1
                # 만약 바꾼 딕셔너리 값이 0 인경우 무시하고 그 외인 경우 갯수를 2로나눈 몫만큼 곱해서 answer 변수에 넣어준다.
                if sorted_dict[k] == 0:
                    pass
                else:
                    answer = answer + k*(sorted_dict[k]//2)
            # 짝수인 경우
            else:
                # 몫이 0인 경우 갯수가 1번 나왔다는 의미이므로 (사실상 불필요) k 한개만 더해준다
                if v//2 == 0:
                    answer = answer + k
                else:
                    answer = answer + k*(v//2)
            # 만약 cnt 값이 2보다 큰 경우 펠린드롬이 될 수 없다.
            if cnt >= 2:
                print("I'm Sorry Hansoo")
                answer = ""
                check = ""
                break
        if answer != "":
            print(answer+check+answer[::-1])