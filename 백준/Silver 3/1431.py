N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input())

for i in range(N-1):
    for j in range(i+1,N):
        i_length = len(word_list[i])
        j_length = len(word_list[j])
        if i_length != j_length:
            if i_length > j_length:
                temp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp
        else:
            num = "0123456789"
            if not word_list[i].isalpha() and not word_list[j].isalpha():
                total_1 = 0
                total_2 = 0
                for k in word_list[i]:
                    if k in num:
                        total_1 += int(k)

                for l in word_list[j]:
                    if l in num:
                        total_2 += int(l)

                if total_1 > total_2:
                    temp = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = temp
                elif total_2 == total_1:
                    if word_list[i] > word_list[j]:
                        temp = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = temp
            else:
                if word_list[i].isalpha() and word_list[j].isalpha():
                    if word_list[i] > word_list[j]:
                        temp = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = temp
                elif not word_list[i].isalpha() and word_list[j].isalpha():
                    temp = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = temp
for _ in word_list:
    print(_)