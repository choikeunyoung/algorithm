T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []
    
    for i in word:
        if i == "(" or i == "{":
            stack.append(i)
        elif i == ")":
            if stack:
                check = stack.pop()
                if check != "(":
                    print(f"#{tc} 0")
                    break
            else:
                print(f"#{tc} 0")
                break
        elif i == "}":
            if stack:
                check = stack.pop()
                if check != "{":
                    print(f"#{tc} 0")
                    break
            else:
                print(f"#{tc} 0")
                break
    else:
        if stack:
            print(f"#{tc} 0")
        else:
            print(f"#{tc} 1")