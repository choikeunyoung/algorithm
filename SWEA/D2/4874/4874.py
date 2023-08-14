T = int(input())

for tc in range(1, T+1):
    words = input().split()
    stack = []
    flag = 0
    for word in words:
        if word == "+":
            if len(stack) >= 2:
                A = stack.pop()
                B = stack.pop()
                stack.append(A+B)
            else:
                flag = 1
                break
        elif word == "/":
            if len(stack) >= 2:
                A = stack.pop()
                B = stack.pop()
                stack.append(B/A)
            else:
                flag = 1
                break
        elif word == "*":
            if len(stack) >= 2:
                A = stack.pop()
                B = stack.pop()
                stack.append(A*B)
            else:
                flag = 1
                break
        elif word == "-":
            if len(stack) >= 2:
                A = stack.pop()
                B = stack.pop()
                stack.append(B-A)
            else:
                flag = 1
                break
        elif word == ".":
            if stack:
                ans = stack.pop()
            else:
                flag = 1
                break
        else:
            stack.append(int(word))

    if stack or flag == 1:
        print(f"#{tc} error")
    else:
        print(f"#{tc} {int(ans)}")