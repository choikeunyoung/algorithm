L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
math_day = (A + C - 1) // C  # 올림 처리
word_day = (B + D - 1) // D  # 올림 처리
max_day = max(math_day, word_day)
print(L - max_day)
