N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input())

for i in range(N-1):
    for j in range(i+1,N):
        if len(word_list[i]) > len(word_list[j]):
            temp = word_list[i]
            word_list[i] = word_list[j]
            word_list[j] = temp
        elif len(word_list[i]) == len(word_list[j]):
            total_1 = 0
            flag_1 = 0
            total_2 = 0
            flag_2 = 0
            for k in "0123456789":
                if k in word_list[i]:
                    total_1 += int(k)
                elif k not in word_list[i]:
                    flag_1 += 1
                if k in word_list[j]:
                    total_2 += int(k)
                elif k not in word_list[j]:
                    flag_2 += 1
            if (total_1 == 0 and flag_1 == 10) or (total_2 == 0 and flag_2 == 10):
                if word_list[i] > word_list[j]:
                    temp = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = temp
            else:
                if total_1 > total_2:
                    temp = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = temp
print(word_list)