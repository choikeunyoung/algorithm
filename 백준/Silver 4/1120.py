word_1,word_2 = input().split()

if len(word_1) == len(word_2):
    cnt = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            cnt += 1
    print(cnt)
else:
    word_1_length = len(word_1)
    word_2_length = len(word_2)
    ans_list = []
    for j in range(word_2_length-word_1_length+1):
        cnt = 0
        for k in range(word_1_length):
            if word_1[k] != word_2[j+k]:
                cnt += 1
        ans_list.append(cnt)
    print(min(ans_list))