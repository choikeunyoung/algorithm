N = int(input())

for _ in range(N):
    word = input()
    if len(word) == 1:
        print(word*2)
    else:
        print(word[0],end="")
        print(word[-1])