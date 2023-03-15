T = int(input())
for _ in range(T):
    word = input()
    pos = 0
    stack = []
    for i in word:
        if i == "<":
            pos -= 1
        elif i == ">":
            pos += 1
        elif i == "-":
            if pos >= len(stack):
                stack.pop()
            else:
                stack.pop(pos-1)
        else:
            if pos < len(stack):
                if pos < 0:
                    pos = 0
                if stack:
                    stack.insert(pos-1,i)
                else:
                    stack.append(i)
            elif pos >= len(stack):
                pos = len(stack) - 1
                stack.append(i)
            pos += 1
    for j in stack:
        print(j,end="")
    print()