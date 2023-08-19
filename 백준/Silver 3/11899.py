words = input()

stack = []

for word in words:
    # 스택에 값이 있을때
    if stack:
        # 만약 닫는 괄호의 경우
        if word == ")":
            # 여는 괄호가 스택의 top 에 있으면 pop
            if stack[-1] == "(":
                stack.pop()
            # 외의 경우 append
            else:
                stack.append(word)
        else:
            stack.append(word)
    else:
        stack.append(word)
# 최종적으로 stack 에 남은 괄호 갯수 출력
print(len(stack))