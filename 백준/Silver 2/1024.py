N, L = map(int,input().split())
# 수학적 귀납법
# N = (x+1) + (x+2) + ... (x+L) => Lx + (L(L+1)/2)
# 리스트 길이가 L ~ 100 까지 증가
for i in range(L,101):
    # N 의 값을 구하기 위해서는 x 개만큼 L이 있고 나머지 1~L까지 합은 L*(L+1)/2 로 나타낼 수 있다.
    x = N - ((i * (i+1))/2)
    # 이렇게 식에 맞게 코드를 작성하여 변수에 할당하면 x 값을 구할 수 있고
    # 만약 x 값이 i 로 나누어 떨어진다면
    if x % i == 0:
        # k 값이 x를 i로 나눈 몫에 +1 을해준다
        k = x//i + 1
        # 이 k 값이 음수가 아닐 경우 k ~ (k+i-1) 까지 출력한다.
        if k >= 0:
            for j in range(i):
                print(int(k+j),end=" ")
            # 조건이 끝나면 break 를 걸어서 더이상 찾지 않도록 한다.
            break
# 만약 끝까지 탐색했는데 값이 없는경우 -1 출력
else:
    print(-1)