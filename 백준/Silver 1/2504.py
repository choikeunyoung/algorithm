info = input().strip()
stack = []
check = ""
flag = 0
number = 0

for i in info:
    if i == "(":
        stack.append(i)
    elif i == "[":
        stack.append(i)
    elif i == ")":
        if "(" not in stack:
            flag = 1
            break
        else:
            check = stack.pop(-1)
        if check == "[":
            flag = 1
            break
        elif check == "(":
            stack.append(2)
        else:
            word_check = stack.pop(-1)
            if len(stack) == 0:
                stack.append(check*2)
            else:
                if word_check == "[":
                    flag = 1
                    break
                elif word_check == "(":
                    stack.append(check*2)
                else:
                    stack.pop(-1)
                    stack.append((check+word_check)*2)
    elif i == "]":
        if "[" not in stack:
            flag = 1
            break
        else:
            check = stack.pop(-1)
        if check == "(":
            flag = 1
            break
        elif check == "[":
            stack.append(3)
        else:
            word_check = stack.pop(-1)
            if len(stack) == 0:
                stack.append(check*3)
            else:
                if word_check == "(":
                    flag = 1
                    break
                elif word_check == "[":
                    stack.append(check*3)
                else:
                    stack.pop(-1)
                    stack.append((check+word_check)*3)
    else:
        flag = 1
        break
    print(stack)

if flag == 1:
    print(0)
else:
    if "[" in stack or "(" in stack:
        print(0)
    else:
        print(sum(stack))