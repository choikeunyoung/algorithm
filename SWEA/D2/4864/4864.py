T = int(input())

for tc in range(1, T+1):
    check_word = input()
    word = input()
    check = 0
    word = word.replace(check_word,"1")
    for i in word:
        if i == "1":
            check = 1
            break
    
    if check == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")