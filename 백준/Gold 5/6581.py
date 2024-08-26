import sys

ans = []
# input으로 들어오는 대로 받기
for words in sys.stdin:
    # 공백 제거하고 구분하여 리스트에 추가
    for word in words.strip().split():
        ans.append(word)
# 정답 출력할 변수
answer = ""
# 리스트 안을 순회
for an in ans:
    # 개행 태그인 경우 이때까지 저장한 문자 출력 후 초기화
    if an == "<br>":
        print(answer)
        answer = ""
        continue
    # --- 구분선 태그인 경우
    if an == "<hr>":
        # 저장한 문자가 있으면 출력 후 - 80 줄 추가
        if answer:
            print(answer)
        print("-"*80)
        answer = ""
        continue
    # 저장한 문자 + 들어온 문자 + 공백의 길이가 80줄이 넘는 경우 저장한 문자 출력 후 새로운 문자로 초기화
    if len(answer) + len(an) + 1 > 80:
        print(answer)
        answer = an
    else:
        # 저장된 문자가 있는경우 공백 추가 후 문자 추가
        if answer:
            answer += " "
        answer += an
# 저장된 문자가 남아있는 경우 출력
if answer:
    print(answer)