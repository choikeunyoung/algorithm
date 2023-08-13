N = int(input())

ans = 1
# 1 ~ N 값까지 반복문을 통해서 곱해나감
for i in range(1,N+1):
    # ans 값의 곱에 10^13 의 나머지를 계산해준다.
    # N값이 1,000,000 까지 들어오기 때문에 10^6 * 10^6 + 1의 값까지 10의 배수의 나머지를 취해준다.
    ans = (ans*i) % (10**13)
    # 만약 곱한 ans 가 10으로 나눠질 경우
    if ans % 10 == 0:
        # ans 의 10의 몫을 계속 구한다.
        while ans % 10 == 0:
            ans //= 10
# 출력을 위해 문자열로 변경
ans = str(ans)
# 끝에서 5자리 출력
ans_length = len(ans)

print(ans[ans_length-5:])