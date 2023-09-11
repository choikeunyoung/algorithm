N = input()

N = str(int(N) + 1)
# N의 길이 변수에 저장
N_length = len(N)
# N을 슬라이싱해서 변수에 저장할 변수
ans = ""
# N의 길이가 짝수인 경우와 홀수인 경우
if len(N) % 2 == 0:
    # 중앙값과 중앙값 이후의 값이 대칭이면 N 출력
    if N[:N_length//2] == N[N_length:N_length//2-1:-1]:
        print(N)
    # 외의 경우
    else:
        # ans 라는 값에 12 / 21 이런 형식으로 값을 저장
        ans = N[:N_length//2] + N[:N_length//2][::-1]
        # 인트로 변환한 값이 N보다 클 경우 ans 출력
        if int(ans) >= int(N):
            print(ans)
        # 작을 경우
        else:
            # 가운데 값이 9 인 경우
            if N[N_length//2] == "9":
                # 가운데 값에 맞는 10**제곱값을 더해준 후
                N = str(int(N) + 10**(N_length//2))
                # N의 길이가 짝 => 홀로 바뀐 경우
                if len(N) > N_length:
                    # N 의 가운데 값 기준으로 대칭으로 만든 후 출력
                    N = N[:N_length//2+1] + N[:N_length//2][::-1]
                    print(N)
                # 변하지 않았을 경우 앞뒤 대칭으로 만든 값 출력
                else:
                    print(N[:N_length//2]+N[:N_length//2][::-1])
            # 가운데 값이 9가 아닌 경우
            else:
                # N의 가운데값 +1 한 후 대칭된 값 출력
                ans = str(int(ans) + 10**(N_length//2))
                print(ans[:N_length//2]+ans[:N_length//2][::-1])
# 홀수인 경우
else:
    # 앞뒤 대칭이면 바로 출력
    if N[:N_length//2] == N[N_length//2+1:N_length//2-1:-1]:
        print(N)
    # 대칭이 아닐 경우
    else:
        # ans 에 대칭되게 값을 넣은 후
        ans = N[:N_length//2+1] + N[:N_length//2][::-1]
        # ans 와 N의 크기를 비교해 ans 값이 더 큰 경우 ans 바로 출력
        if int(ans) >= int(N):
            print(ans)
        # ans 값이 더 작은 경우
        else:
            # 만약 중앙값이 9 인 경우
            if N[N_length//2] == "9":
                # N의 값에 중앙값 +1 해준 값 저장
                N = str(int(N) + 10**(N_length//2))
                # 더한 N 값이 홀 => 짝이 된 경우
                if len(N) > N_length:
                    # 대칭되게 값 저장 후 출력
                    N = N[:N_length//2] + N[:N_length//2][::-1]
                    print(N)
                # 외의 경우 대칭되게 값출력
                else:
                    print(N[:N_length//2+1]+N[:N_length//2][::-1])
            # 9가 아닌 경우 가운데 값 +1 한 후 대칭되게 출력
            else:
                print(int(ans) + 10**(N_length//2))