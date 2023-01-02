N = int(input())
word_dict = []
for _ in range(N):
    word = input()
    if word not in word_dict:
        word_dict.append(word)



for i in range(len(word_dict)-1):
    for j in range(i+1,len(word_dict)):
        if len(word_dict[i]) > len(word_dict[j]):
            word_dict[i] = 