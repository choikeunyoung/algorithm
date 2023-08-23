T = int(input())

for tc in range(1,T+1):
    word = list(input())
    word_length = len(word)
    change_word = ["0"]*word_length
    cnt = 0
    while change_word != word:
        for i in range(word_length):
            if word[i] != change_word[i]:
                for j in range(i,word_length):
                    if change_word[j] == "0":
                        change_word[j] = "1"
                    else:
                        change_word[j] = "0"
                cnt += 1
                break
    print(f"#{tc} {cnt}")