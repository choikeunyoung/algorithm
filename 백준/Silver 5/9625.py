
K = int(input())
ans = dp()
# 들어온 K의 값 출력

print(*ans[K])

def dp():
    # 정답 리스트
    ans_list = [[1,0]]
    # K가 45까지 들어오기때문에
    for _ in range(45):
        ans_list.append([ans_list[-1][1],ans_list[-1][0]+ans_list[-1][1]])
    return ans_list