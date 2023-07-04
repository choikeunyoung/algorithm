word = input()
word_check = [0]*26
for i in word:
    word_check[ord(i)-97] += 1
print(*word_check)