# input 문자열
info = input()
# 문자를 담을 리스트
stack = []
# 갯수 체크
cnt = 0
# enumerate 로 index와 value 값을 가져옴
for i,v in enumerate(info):
    # 여는 괄호일 경우
    if v == "(":
        # 스택에 index 값 추가
        stack.append(i)
        # 레이저인지 막대인지 모르지만 갯수 추가
        cnt += 1
    # 닫는 괄호가 나왔을 경우
    else:
        # check 라는 변수에 stack의 제일 뒤값을 뽑아본다.
        check = stack.pop(-1)
        # 만약 뽑은 값의 +1 과 닫는괄호의 인덱스가 같은경우 => () 인 경우라서 레이저다
        if check+1 == i:
            # cnt로 체크해둔 값을 -1 해준 후 그때까지 저장된 스택의 길이를 더해준다.
            cnt -= 1
            cnt += len(stack)
print(cnt)