word = input()

cnt = 0
# AAAA 4번 사용 대체 변수
A = "AAAA"
# BB 대체 변수
B = "BB"
# 체크하는 리스트 생성
ans_list = []

for i in word:
    # 만약 . 인 경우
    if i == ".":
        # 그 중에서 4로 나누어지거나 2로 나누어지는 경우 리스트에 추가
        if cnt % 4 == 0 or cnt % 2 == 0:
            ans_list.append(cnt)
        # 그 외의 경우는 -1 출력 후 브레이크
        else:
            print(-1)
            break
        # 리스트에 점 추가
        ans_list.append(i)
        # 값 초기화
        cnt = 0
    else:
        cnt += 1
# break 로 나오지 않고 그냥 끝났을 경우
else:
    # 맨 마지막 cnt 값에 대해서 2 or 4 로 안나뉠 경우 -1 출력
    if cnt % 4 != 0 and cnt % 2 != 0:
        print(-1)
    # 그 외의 경우
    else:
        # 리스트에 cnt 값 추가
        ans_list.append(cnt)
        # 리스트 순회하며 조건에 맞도록 출력
        for j in ans_list:
            if j != ".":
                if j % 4 == 0:
                    print(A*(j//4), end="")
                elif j % 2 == 0:
                    print(A*(j//4),end="")
                    print(B*((j%4)//2),end="")
            else:
                print(j, end="")