word = input()
num_stack = []
other_stack = []
for i in word:
    ans = 0
    if i == ")":
        while num_stack[-1] != "(":
            check_num = num_stack.pop()
            if isinstance(check_num, int):
                ans += check_num
            else:
                other_stack.append(check_num)
        num_stack.pop()
        check = len(other_stack) + ans
        num_stack.append(int(num_stack.pop())*check)
        other_stack = []
    else:
        num_stack.append(i)
answer = ""
ans = 0
for i in num_stack:
    if isinstance(i,int):
        ans += i
    else:
        answer += i
if answer != "":
    print(len(answer)+ans)
else:
    print(ans)