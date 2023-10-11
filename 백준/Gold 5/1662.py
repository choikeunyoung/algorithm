word = input()
num_stack = []
other_stack = []
ans = 0
for i in word:
    if i == ")":
        while num_stack[-1] != "(":
            other_stack.append(num_stack.pop())
        num_stack.pop()
        check = len(other_stack)
        check = int(num_stack.pop())*check
        if ans == 0:
            ans += check
        else:
            ans += check-1
        num_stack.append(str(check))
        other_stack = []
    else:
        num_stack.append(i)

answer = "".join(num_stack)

ans += len(answer)-1
print(ans)