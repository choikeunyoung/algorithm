import sys

sys.stdin = open('input.txt')
words = sys.stdin.read()
words = words.replace('\n',"")
words = words.replace(" ",'')

dict = {}

for i in words:
    for j in i:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
word = []
for k, v in dict.items():
    if max(dict.values()) == v:
        word.append(k)

word.sort()
for l in word:
    print(l,end='')