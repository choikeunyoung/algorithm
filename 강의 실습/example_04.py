# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# ----------오류 코드 ----------------------
# words = list(map(int, input().split()))
# print(words)
# ValueError: invalid literal for int() with base 10: "I'm"


words = list(map(str, input().split()))
print(words)