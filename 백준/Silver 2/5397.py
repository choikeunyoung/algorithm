T = int(input())
for _ in range(T):
    words = input()
    current_pos= 0
    ans = []
    for word in words:
        if word == "<":
            current_pos -= 1
            if current_pos < 0:
                current_pos = 0
        elif word == "-":
            if ans:
                ans.pop(current_pos-1)
        else:
            if word != ">":
                if current_pos == len(ans):
                    ans.append(word)
                else:
                    ans.insert(current_pos,word)
            current_pos += 1
            if current_pos > len(ans):
                current_pos = len(ans)
    answer = "".join(ans)
    print(answer)