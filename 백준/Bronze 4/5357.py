N = int(input())

for _ in range(N):
    word = input()
    answer = ""
    for i in word:
        if answer:
            if answer[-1] != i:
                answer += i
        else:
            answer += i
    print(answer)
