word = input().strip()
word_length = len(word)
answer = []
ans = ""

for i in word:
    if i == "(":
        answer.append(ans)
        ans = ""
    elif i == ")":
        if ans != "":
            check = int(answer.pop())
            rest = check%10
            ans *= rest
            check //= 10
            if check != 0:
                check = str(check)
                ans = check + ans
    else:
        ans += i
print(ans)
if ans == "":
    print(0)
else:
    print(len(ans))