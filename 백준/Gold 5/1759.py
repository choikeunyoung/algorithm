def find_list(num):
    global vowel_cnt
    global consonant
    global list_length
    if list_length == N:
        if num == N-1:
            if ans[-1] == "a" or ans[-1] == "e" or ans[-1] == "i" or ans[-1] == "o" or ans[-1] == "u":
                vowel_cnt += 1
            elif ans[-1] != "a" and ans[-1] != "e" and ans[-1] != "i" and ans[-1] != "o" and ans[-1] != "u":
                consonant += 1
        if vowel_cnt >= 1 and consonant >= 2:
            print("".join(ans))
        if num == N-1:
            if ans[-1] == "a" or ans[-1] == "e" or ans[-1] == "i" or ans[-1] == "o" or ans[-1] == "u":
                vowel_cnt -= 1
            elif ans[-1] != "a" and ans[-1] != "e" and ans[-1] != "i" and ans[-1] != "o" and ans[-1] != "u":
                consonant -= 1
        return
    else:
        for i in range(num,M):
            if word_list[i] == "a" or word_list[i] == "e" or word_list[i] == "i" or word_list[i] == "o" or word_list[i] == "u":
                vowel_cnt += 1
            elif word_list[i] != "a" and word_list[i] != "e" and word_list[i] != "i" and word_list[i] != "o" and word_list[i] != "u":
                consonant += 1
            ans.append(word_list[i])
            list_length += 1
            find_list(i+1)
            ans.pop()
            list_length -= 1
            if word_list[i] == "a" or word_list[i] == "e" or word_list[i] == "i" or word_list[i] == "o" or word_list[i] == "u":
                vowel_cnt -= 1
            elif word_list[i] != "a" and word_list[i] != "e" and word_list[i] != "i" and word_list[i] != "o" and word_list[i] != "u":
                consonant -= 1
N, M = map(int,input().split())

word_list = list(map(str,input().split()))

word_list.sort()
ans = []
list_length = 0
vowel_cnt = 0
consonant = 0

find_list(0)