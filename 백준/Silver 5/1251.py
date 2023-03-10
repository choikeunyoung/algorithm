word = input()
check_list = []
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        split_word = word[:i]
        split_second_word = word[i:j]
        split_third_word = word[j:]
        split_word = split_word[::-1]
        split_second_word = split_second_word[::-1]
        split_third_word = split_third_word[::-1]
        total_word = split_word + split_second_word + split_third_word
        check_list.append(total_word)
print(min(check_list))