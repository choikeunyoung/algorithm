N = input()

# 값을 비교할 문자열 변수 생성
check = ""
# 갯수를 카운트할 변수 생성
cnt = 1

# 문자열 반복 시작
for i in N:
# 처음 값을 시작했을 경우
    if check == "":
# 비교할 문자열 변수에 i 값을 넣어줌
        check = i
# 처음이 아닌 경우
    else:
# 만약 i 값이랑 이전의 i 값이 다를경우 cnt + 1
        if check != i:
            cnt += 1
# 모든 조건문이 끝나면 check에 i 값 넣어줌
        check = i
# cnt 값이2 이상 즉 변화가 있을경우
if cnt >= 2:
# cnt // 2 값을 출력
    print(cnt//2)
# 초기 cnt 값이랑 변화가 없을 경우 0 출력
elif cnt == 1:
    print(0)