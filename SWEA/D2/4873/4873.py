T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []
    flag = 0
    word_length = len(word)
    for i in word:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f"#{tc}",len(stack))