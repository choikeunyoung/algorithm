T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(str,input())) for _ in range(N) ]
    flag = 0
    for i in range(N):
        word = "".join(matrix[i])
        word_length = len(word)
        if word_length == M:
            reverse_word = "".join(list(reversed(word)))
            if word == reverse_word:
                print(f"#{tc} {word}")
                flag = 1
                break
        else:
            for j in range(word_length-M+1):
                reverse_word = "".join(list(reversed(word[j:j+M])))
                
                if word[j:j+M] == reverse_word:
                    print(f"#{tc} {word[j:j+M]}")
                    flag = 1
                    break
        if flag == 1:
            break
    
    if flag == 0:
        for i in range(N):
            for j in range(N-M+1):
                word = ""
                for k in range(M):
                    word += matrix[j+k][i]
                reverse_word = "".join(list(reversed(word)))
                if word == reverse_word:
                    flag = 1
                    print(f"#{tc} {word}")
                    break
            if flag == 1:
                break