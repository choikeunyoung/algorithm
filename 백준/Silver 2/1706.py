R, C = map(int,input().split())


matrix = [ input() for _ in range(R) ]

word_list = []

for i in matrix:
    middle_list = i.split("#")
    if len(middle_list) > 1:
        max_cnt = 0
        check = ""
        for j in middle_list:
            if j != "":
                if max_cnt < len(j):
                    max_cnt = len(j)
                    word = j
        if max_cnt > 1:
            word_list.append(word)
    else:
        if len(i) > 1:
            word_list.append(i)

for i in range(C):
    word = ""
    max_cnt = 0
    check = ""
    for j in range(R):
        if matrix[j][i] != "#":
            word += matrix[j][i]
        elif matrix[j][i] == "#":
            if max_cnt < len(word):
                max_cnt = len(word)
                check = word
            word = ""
    if word != "":
        if max_cnt < len(word):
            max_cnt = len(word)
            check = word
    if max_cnt != 1:
        word_list.append(check)

for k in sorted(word_list):
    if k != "":
        print(k)
        break