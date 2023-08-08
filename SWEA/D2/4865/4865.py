T = int(input())

for tc in range(1, T+1):
    check_word = input()
    word = input()
    
    word_dict = {}
    max_cnt = 0
    
    for i in check_word:
        cnt = 0
        for j in word:
            if i == j:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")