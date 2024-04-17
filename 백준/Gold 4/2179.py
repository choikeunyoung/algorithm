import sys

input = sys.stdin.readline

N = int(input())

word_list = []

max_length = 0
for _ in range(N):
    words = input().strip()
    if len(words) > max_length:
        max_length = len(words)
    word_list.append((len(words),words))

check_list = sorted(word_list)
answer = ""
for i in range(max_length):
    for word in word_list:
        if word[0] >= i:
            answer