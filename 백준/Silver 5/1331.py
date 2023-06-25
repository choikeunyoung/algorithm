word_list = []
for _ in range(36):
    word = input()
    if word in word_list:
        print("Invalid")
        break
    else:
        word_list.append(word)
else:
    start = word_list[0]
    end = word_list[-1]
    answer_list = []
