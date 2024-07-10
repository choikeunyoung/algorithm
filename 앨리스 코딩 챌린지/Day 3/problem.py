word = input()

stack = []

open_cnt = 0

for i in word:
    if i == "(":
        open_cnt += 1
        stack.append(i)
    elif i == ")":
        open_cnt -= 1
        ans = ""
        while stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
        calculate = int(stack.pop())
        stack.append(calculate*ans)
    else:
        stack.append(i)
answer = "".join(stack)
print(len(answer))