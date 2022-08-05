import sys

sys.stdin = open("_괄호짝짓기.txt")

for i in range(1,11):
    n = int(sys.stdin.readline())
    char = str(sys.stdin.readline())
    small_bracket = 0
    mid_bracket = 0
    big_bracket = 0
    bracket = 0
    for j in char:
        if j == "(":
            small_bracket+=1
        elif j == '[':
            big_bracket+=1
        elif j == '{':
            mid_bracket+=1
        elif j == '<':
            bracket+=1
        elif j == '>':
            bracket-=1
        elif j == '}':
            mid_bracket-=1
        elif j == ']':
            big_bracket-=1
        elif j == ')':
            small_bracket-=1
    if small_bracket == 0 and big_bracket == 0 and mid_bracket == 0 and bracket == 0:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")