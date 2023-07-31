N = int(input())

word_list = []
answer = 0

for _ in range(N):
    word_list.append(input())

check_list = [word_list[0]]

for i in range(len(check_list[-1])):
    start_word = check_list[0][0:i]
    middle_word = check_list[0][i:i+1]
    last_word = check_list[0][i+1:]
    check_list.append(start_word+last_word)
    check_list.append(start_word+middle_word+middle_word+last_word)

flag = False
for i in check_list:
    word_dict = {}
    word_length = len(i)
    for j in i:
        if j in word_dict:
            word_dict[j] += 1
        else:
            word_dict[j] = 1
            
    for k in word_list[1:]:
        check = 0
        check_cnt = 0
        check_length = len(k)
        if flag == False:
            if check_length == word_length:
                for l in k:
                    if l in word_dict:
                        word_dict[l] -= 1
                    else:
                        check += 1

                    if check > 1:
                        break
                    
                for l in word_dict.values():
                    if l > 0 or l < 0:
                        check_cnt += 1

                if (check == 1 and check_cnt == 1) or (check_cnt == 0 and check == 0):
                    answer += 1
            elif check_length + 1 == word_length:
                for l in k:
                    if l in word_dict:
                        word_dict[l] -= 1
                    else:
                        check += 1

                    if check > 1:
                        break
                    
                for l in word_dict.values():
                    if l > 0 or l < 0:
                        check_cnt += 1

                if (check == 0 and check_cnt == 1):
                    answer += 1
            elif check_length - 1 == word_length:
                for l in k:
                    if l in word_dict:
                        word_dict[l] -= 1
                    else:
                        check += 1

                    if check > 1:
                        break
                    
                for l in word_dict.values():
                    if l > 0 or l < 0:
                        check_cnt += 1

                if (check == 1 and check_cnt == 0):
                    answer += 1
        else:
            if word_length == check_length:
                for l in k:
                    if l in word_dict:
                        word_dict[l] -= 1
                    else:
                        check += 1

                    if check >= 1:
                        break
                    
                for l in word_dict.values():
                    if l < 0 or l > 0:
                        check_cnt += 1

                if check_cnt == 0 and check == 0:
                    answer += 1
        flag = True
print(answer)