X = int(input())
# 막대는 64의 약수로만 나눠진다.
bars = [1,2,4,8,16,32,64]
# X와 값을 비교할 변수 생성
total = 0
# 갯수 세는 변수 생성
cnt = 0
# 리스트 거꾸로 출력
for i in bars[::-1]:
    # 만약 X가 i 보다 큰 경우
    if X > i:
        #값을 더해준다
        total += i
        # 값이 X보다 큰 경우
        if total > X:
            # 다시 값을 뺸다
            total -= i
        # 그 외의 경우 cnt를 증가시킨다.
        else:
            cnt += 1
    # 만약 X 가 i 랑 같은 경우 즉 리스트 값인경우 break를 시켜준다
    elif X == i:
        cnt += 1
        break
print(cnt)