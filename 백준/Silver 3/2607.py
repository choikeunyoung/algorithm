import copy

N = int(input())

word_list = []
cnt = 0

for _ in range(N):
    word = input()
    word_list.append(word)

first_word = word_list[0]

check_list = [first_word]

for i in range(len(first_word)):
    start_word = first_word[:i]
    middle_word = first_word[i:i+1]
    last_word = first_word[i+1:]
    first_add_word = start_word+middle_word+middle_word+last_word
    second_add_word = start_word+last_word
    check_list.append(first_add_word)
    check_list.append(second_add_word)
answer_list = []
for i in range(1,N):
    word_length = len(word_list[i])
    word_dict = {}
    for k in word_list[i]:
        if k in word_dict:
            word_dict[k] += 1
        else:
            word_dict[k] = 1
    for j in check_list:
        check_dict = {}
        total = 0
        check_dict = copy.deepcopy(word_dict)
        if len(j) == word_length:
            word_check = 0
            for l in j:
                if l in check_dict:
                    check_dict[l] -= 1
                else:
                    word_check += 1
            for v in check_dict.values():
                if v >= 0:
                    total += v
                else:
                    if v == -1 and word_check == 0:
                        word_check += 1
                    else:
                        total = -10
                    break
            if total == 0 or (total == 1 and word_check == 1 ):
                if word_list[i] not in answer_list:
                    cnt += 1
                    answer_list.append(word_list[i])
                break
        print(check_dict,word_dict,total)
print(cnt,check_list,answer_list)

# 길이가 같을때 조건을 수정하면 해결될 것 같음.