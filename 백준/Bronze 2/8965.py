import sys

input = sys.stdin.readline

N = int(input())

sequences = []

for _ in range(N):
    sequences.append(input().split())


for word in sequences:
    word_length = len(word[-1])
    next_word = word[-1]+word[-1]
    answer = [word[-1]]
    print(next_word)
    for i in range(1,word_length):
        print(next_word[i:i+word_length],"i")
        if next_word[i:i+word_length] < answer[-1]:
            answer = next_word[i:i+word_length]
    print(answer)
