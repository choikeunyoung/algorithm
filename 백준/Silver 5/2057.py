N = int(input())

DP = [0, 1, 2]
# 팩토리얼 값이 10의 19승이 되기 전까지 추가
for i in range(3, 21):
    check = DP[-1] * i
    if check <= 10**19:
        DP.append(check)
# 끝의 값을 구해서
res = DP[-1]
# 끝에서부터 값을 나눠줌
for i in range(20, 0, -1):
    res //= i
    # 만약 N값보다 작거나 같으면 N에 res 를 빼준다.
    if res <= N:
        N -= res
# N이 0인 경우 YES아니면 NO
if N == 0:
    print("YES")
else:
    print("NO")
